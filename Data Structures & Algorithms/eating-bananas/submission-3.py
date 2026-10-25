class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = max(piles)

        if h == n:
            return m

        l, r = 1, m
        res = 0

        while l <= r:
            mid = (l + r) // 2 
            time = self.calculateTotalTime(mid, piles)
            if time <= h:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res


    def calculateTotalTime(self, val, piles):
        res = 0
        for pile in piles:
            res += math.ceil(pile/val)
        return res
