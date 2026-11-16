class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        l_idx = len(nums) - 1
        valid = set([l_idx])
        m_valid = l_idx
        for i in range(len(nums) - 2, -1, -1):
            m_jump = nums[i] + i
            dp[i] = (m_jump >= l_idx) or (m_jump in valid) or  (m_jump >= m_valid)
            if dp[i]:
                valid.add(i)
                if i < m_valid:
                    m_valid = i
        
        return dp[0]
                