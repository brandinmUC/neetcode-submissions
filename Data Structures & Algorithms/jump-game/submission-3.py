class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        l_idx = len(nums) - 1
        valid = set([l_idx])
        m_valid = l_idx
        for i in range(len(nums) - 2, -1, -1):

            dp[i] = (nums[i] + i >= l_idx) or (nums[i] + i in valid) or  (nums[i] + i >= m_valid)
            if dp[i]:
                valid.add(i)
            m_valid = min(valid)
        
        # print(dp)
        return dp[0]
                