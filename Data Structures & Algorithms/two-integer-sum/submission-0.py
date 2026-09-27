class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            res = target - num
            if res in seen:
                return [seen[res], idx]
            seen[num] = idx
                