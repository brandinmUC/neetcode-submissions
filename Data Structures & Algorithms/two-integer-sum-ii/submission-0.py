class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(numbers):
            res = target - num
            if res in seen:
                return [seen[res] + 1, idx + 1]
            seen[num] = idx