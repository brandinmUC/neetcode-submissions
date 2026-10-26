
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxheap = [] # val, idx

        for r, v in enumerate(nums):
            heapq.heappush(maxheap, (-v, r))
            if r >= k - 1:
                while maxheap[0][1] <= r - k:
                    heapq.heappop(maxheap)
                res.append(-maxheap[0][0])
        
        return res
