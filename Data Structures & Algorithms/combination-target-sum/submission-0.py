class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def dfs(i, lst, tot):
            if tot == target:
                res.append(lst.copy())
                return
            if tot > target or i >= n:
                return

            lst.append(nums[i])
            dfs(i, lst, tot + nums[i])
            lst.pop()
            dfs(i + 1, lst, tot)

        dfs(0, [], 0)
        return res