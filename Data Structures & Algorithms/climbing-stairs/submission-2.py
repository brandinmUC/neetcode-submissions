class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(1, n):
           nxt = one + two
           two = one
           one = nxt
            
        return one
        