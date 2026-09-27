class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
    
        while fast != slow:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False
            

    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n / 10 >= 1:
            q, r = divmod(n, 10)
            n = q
            res += r ** 2
        res += n ** 2
        return res
