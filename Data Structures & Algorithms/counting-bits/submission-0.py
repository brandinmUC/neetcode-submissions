class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            ctr = 0
            icpy = i
            while icpy:
                if icpy & 1:
                    ctr += 1
                icpy >>= 1
            res.append(ctr)
        return res
