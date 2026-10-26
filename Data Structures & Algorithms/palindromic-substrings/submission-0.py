class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(1, len(s) + 1):
            l = 0
            r = l + i
            while r <= len(s):
                sub = s[l:r]
                sub_r = sub[::-1]
                if sub == sub_r:
                    res += 1
                l += 1
                r += 1
        
        return res

