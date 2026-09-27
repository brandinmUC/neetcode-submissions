class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 1

        if not nums:
            return 0

        while nset:
            counter = 0
            low = min(nset)
            curr = low
            while curr in nset:
                counter += 1
                nset.remove(curr)
                curr += 1
            res = max(res, counter)
        
        return res

            