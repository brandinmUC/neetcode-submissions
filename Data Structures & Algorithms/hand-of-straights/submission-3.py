class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
            
        freq = {}
        
        for i in hand:
            freq[i] = freq.get(i, 0) + 1
        
        keys = list(freq.keys())
        heapq.heapify(keys)

        curr, nxt = keys[0], 0
        count = 0
        while keys:
            nxt = curr + 1
            if curr not in freq:
                return False
            freq[curr] -= 1
            count += 1
            if freq[curr] == 0:
                heapq.heappop(keys)
            if count == groupSize:
                count = 0
                if keys:
                    curr = keys[0]
            else:
                curr = nxt
        return True if count == 0 else False
