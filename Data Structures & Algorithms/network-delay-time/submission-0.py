class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for source, target, time in times:
            edges[source].append((target, time))
        
        minheap = [(0, k)] # weight, src node
        seen = set()
        t = 0

        while minheap:
            w, src = heapq.heappop(minheap) # weight, src node
            if src not in seen:
                seen.add(src)
                t = max(t, w)

                for nt, nw in edges[src]: # neighbor target (src) & weight
                    if nt not in seen: 
                        heapq.heappush(minheap, (w + nw, nt))
                heapq.heapify(minheap)

        return t if len(seen) == n else -1



