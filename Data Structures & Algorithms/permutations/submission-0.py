class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nlen = len(nums)
    
        def backtrack(choice, rest):
            nonlocal nlen

            if len(choice) == nlen:
                res.append(choice)
                return

            for i in range(len(rest)):
                n = rest[:i] + rest[i+1:]
                backtrack(choice + [rest[i]], n)

        for i in range(nlen):
            n = nums[:i] + nums[i+1:]
            backtrack([nums[i]], n)

        return res