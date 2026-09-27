class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for c in s:
            if c.isalnum():
                st += c
        st = st.lower()
        return st == st[::-1]
         