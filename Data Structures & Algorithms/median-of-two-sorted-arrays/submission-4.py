import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        tot = len(nums1) + len(nums2)
        half = tot // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = ((r - l) // 2) + l
            j = half - i - 2

            if i >= 0:
                Aleft = A[i]
            else:
                Aleft = -math.inf
            if (i + 1) < len(A):
                Aright = A[i + 1]
            else:
                Aright = math.inf
            if j >= 0:
                Bleft = B[j]
            else:
                Bleft = -math.inf
            if (j + 1) < len(B):
                Bright = B[j + 1]
            else:
                Bright = math.inf

            if Aleft <= Bright and Bleft <= Aright:
                if tot % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                return min(Aright, Bright)
            elif Aleft > Bright:
                    r = i - 1
            else:
                    l = i + 1