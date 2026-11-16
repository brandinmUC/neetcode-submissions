class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l_idx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            m_jump = nums[i] + i #max jump
            if m_jump >= l_idx: 
                l_idx = i
        return l_idx == 0
                