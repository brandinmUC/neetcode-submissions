class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest = 0
        slen = len(s)

        for i in range(slen): # idx
            #odd
            l, r = i, i
            while l >= 0 and r < slen and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1

            # even
            el, er = i - 1, i
            while el >= 0 and er < slen and s[el] == s[er]:
                if (er - el + 1) > longest:
                    longest = er - el + 1
                    res = s[el: er + 1]
                el -= 1
                er += 1

        return res
