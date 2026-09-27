class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
       
        while l < r:
            lval = numbers[l]
            rval = numbers[r]
            if lval + rval > target:
                r -= 1
            elif lval + rval < target:
                l += 1
            else:
                return [l + 1, r + 1]
