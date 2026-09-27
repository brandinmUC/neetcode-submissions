class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}

        if len(s) != len(t):
            return False

        for sc in s:
            s_chars[sc] = s_chars.get(sc, 0) + 1 
        
        for tc in t:
            if tc not in s_chars:
                return False
            s_chars[tc] -= 1
            if s_chars[tc] == 0:
                del s_chars[tc]

        return len(list(s_chars.keys())) == 0
            

