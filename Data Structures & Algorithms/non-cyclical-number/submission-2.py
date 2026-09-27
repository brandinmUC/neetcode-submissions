class Solution:
    def isHappy(self, n: int) -> bool:
        curr = 0
        l = set()
        while curr != 1:
            curr = self.sumOfSquares(n)
            if curr == 1:
                return True
            if curr in l:
                return False
            l.add(curr)
            n = curr
            

    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n / 10 >= 1:
            q, r = divmod(n, 10)
            n = q
            res += r ** 2
        res += n ** 2
        return res
