class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        maxsum = -math.inf
        total = 0
        for i in nums:
            if i > total + i:
                total = i
            else:
                total += i
            print(total)
            maxsum = max(maxsum, total, i)
        return maxsum
            