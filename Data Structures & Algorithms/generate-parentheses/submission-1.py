class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(perm, o, c): # permutation, num_open, num_closed
            print(perm, o, c)

            if c > o:
                return

            if o == n:
                while c < o:
                    perm += ")" 
                    c += 1 
                res.append(perm)
                return

            backtrack(perm + ")", o, c + 1)
            backtrack(perm + "(", o + 1, c)
            

        backtrack("(", 1, 0)
        return res
