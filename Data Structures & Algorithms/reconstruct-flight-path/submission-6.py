class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        stack = ["JFK"]
        res = []
        adjLst = defaultdict(list)

        for dpt, arr in sorted(tickets)[::-1]:
            adjLst[dpt].append(arr)

        while stack:
            curr = stack[-1]
            if not adjLst[curr]:
                res.append(stack.pop())
            else:
                stack.append(adjLst[curr].pop())

        return res[::-1]
