class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = max(piles)

        l, r = 1, m
        res = 0

        while l <= r:
            mid = (l + r) // 2 
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time <= h:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res
