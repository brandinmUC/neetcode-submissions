class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        seen = set()
        while r < len(s):
            c = s[r]
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            res = max(res, r - l + 1)
            r += 1
        return res
        