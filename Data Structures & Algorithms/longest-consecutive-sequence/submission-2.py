class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 1

        if not nums:
            return 0

        for num in nset:
            if (num - 1) not in nset:
                counter = 1
                while num + counter in nset:
                    counter += 1
                res = max(res, counter)
        
        return res

            