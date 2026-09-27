class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            ctr = 0
            for j in range(32):
                if (1 << j) & i:
                    ctr += 1
            res.append(ctr)
        return res
