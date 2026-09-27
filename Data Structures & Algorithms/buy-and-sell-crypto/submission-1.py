class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for r in range(1, len(prices)):
            lp = prices[l]
            rp = prices[r]
            if lp < rp:
                res = max(rp - lp, res)
            else:
                l = r
        return res