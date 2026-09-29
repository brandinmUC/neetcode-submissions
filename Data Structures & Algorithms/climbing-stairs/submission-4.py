class Solution:
    def climbStairs(self, n: int) -> int:
        n_minus_one, n_minus_two = 1, 1
        for i in range(1, n):
           fib = n_minus_one + n_minus_two # fibonacci numbers
           n_minus_two = n_minus_one
           n_minus_one = fib
            
        return n_minus_one
        