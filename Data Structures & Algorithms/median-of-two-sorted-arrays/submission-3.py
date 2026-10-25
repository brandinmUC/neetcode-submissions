from decimal import Decimal, ROUND_HALF_UP

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m3 = nums1 + nums2
        m3.sort()
        if len(m3) % 2 == 1:
            return m3[((len(m3) - 0) // 2)]
        return (m3[((len(m3) - 0) // 2)] + m3[((len(m3) - 0) // 2) - 1]) / 2




    def binSearch(self, lst, target):
        l, r = 0, len(lst) - 1
        res = 0
        while l <= r:
            mid = ((r - l) // 2) + l 
            val = lst[mid]
            if val <= target:
                l = mid + 1
                res = val
            else:
                r = mid - 1

        return res