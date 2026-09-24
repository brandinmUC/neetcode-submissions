class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        res = 0
        
        while l < r: 
            if r_max > l_max:
                l += 1
                l_val = height[l]
                l_max = max(l_max, l_val)
                res += l_max - l_val
            else:
                r -= 1
                r_val = height[r]
                r_max = max(r_max, r_val)
                res += r_max - r_val
        return res