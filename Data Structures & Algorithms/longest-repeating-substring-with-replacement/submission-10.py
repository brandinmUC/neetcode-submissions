class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 1
        l = 0
        hmap ={s[l]:1}
        res = 0
        for r in range(1, len(s)):
            val = s[r]
            hmap[val] = hmap.get(val, 0) + 1
            freq = max(hmap.values())
            count += 1
            if count - freq > k:
                hmap[s[l]] -= 1
                l += 1
                count -= 1
        res = max(res, count)
        return res