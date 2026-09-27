class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for l in range(len(prices) - 1):
            lp = prices[l]
            rp = max(prices[l + 1:])
            if lp < rp:
                res = max(rp - lp, res)
        return res
        