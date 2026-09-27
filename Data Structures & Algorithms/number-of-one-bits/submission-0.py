class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        ctr = 0
        for c in n:
            if c == "1":
                ctr += 1
        return ctr