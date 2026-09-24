class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l != r:
            l_val, r_val = heights[l], heights[r]
            area = min(l_val, r_val) * (r - l)
            res = max(res, area)
            if l_val > r_val:
                r -= 1
            else:
                l += 1

        return res
