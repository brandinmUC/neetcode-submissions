class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return max(nums)
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i-2])

        return dp[-1]
 
