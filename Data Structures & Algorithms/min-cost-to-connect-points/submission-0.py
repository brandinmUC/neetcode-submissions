class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjlst = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                m_dist = abs(x1 - x2) + abs(y1 - y2)
                adjlst[i].append([m_dist, j])
                adjlst[j].append([m_dist, i])

        res = 0
        seen = set()
        minheap = [[0, 0]] #cost, points

        while len(seen) < len(points):
            cost, point = heapq.heappop(minheap)
            if point in seen:
                continue
            res += cost
            seen.add(point)
            for neiCost, nei in adjlst[point]:
                if nei not in seen:
                    heapq.heappush(minheap, [neiCost, nei])

        return res