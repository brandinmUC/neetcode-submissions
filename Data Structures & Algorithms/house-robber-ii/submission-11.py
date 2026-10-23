class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return max(nums)
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            return memo[i]
        return max(dfs(0), dfs(1))
 
