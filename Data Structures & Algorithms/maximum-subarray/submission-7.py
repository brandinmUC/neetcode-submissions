class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, total = -math.inf, 0
        
        for i in nums:
            if i > total + i:
                total = i
            else:
                total += i
            maxsum = max(maxsum, total)
        return maxsum
            