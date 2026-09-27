class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        maxheap = stones
        heapq.heapify(maxheap)

        print(maxheap)
        while len(maxheap) > 1:
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)
            if y > x:
                heapq.heappush(maxheap, (x - y))
            

        if maxheap:
            return -maxheap[0]
        else:
            return 0
            