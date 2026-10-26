class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        res = ""
        tmap, window = {}, {} # original dict

        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        
        have, need = 0, len(tmap)
        res, reslen = [-1, -1], math.inf
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in tmap.keys() and window[char] == tmap[char]:
                have += 1
        
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
              
                window[s[l]] -= 1
                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if reslen < math.inf else ""

