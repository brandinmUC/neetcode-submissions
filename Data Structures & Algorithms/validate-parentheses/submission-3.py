class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        o = {"{": "}", "[" : "]", "(":")"}

        for c in s:
            if c in o.keys():
                st.append(c)
            elif st:
                if o[st[-1]] == c:
                    st.pop()
                else:
                    return False
            else:
                return False
        return not st