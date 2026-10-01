class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len:
            return False

        freq = {}

        for c in s1:
           freq[c] = 1 + freq.get(c, 0)
            
        l, r = 0, s1_len
        while r <= s2_len:
            sub = s2[l:r]
            freq_cpy = freq.copy()
            for char in sub:
                if char not in freq_cpy:
                    break
                else:
                    freq_cpy[char] -= 1
                    if freq_cpy[char] == 0:
                        del freq_cpy[char]
            if list(freq_cpy.values()) == []:
                return True
            l += 1
            r += 1
        return False 
