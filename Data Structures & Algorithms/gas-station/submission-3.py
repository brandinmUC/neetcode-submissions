class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
            
        diff = [(x[1] - y, x[0]) for x, y in zip(enumerate(gas), cost)] #diff ,idx
        heapq.heapify_max(diff)

        while diff:
            s = heapq.heappop_max(diff)
            if s[0] < 0:
                return -1
            r = s[1]
            l = r + 1
            if r == len(gas) - 1:
                l = 0

            fuel = s[0]
            while l != r:
                fuel += gas[l]
                fuel -= cost[l]
                if fuel < 0:
                    break
                if l == len(gas) - 1:
                    l = -1
                l += 1
            if fuel >= 0:
                return s[1]
        return -1
