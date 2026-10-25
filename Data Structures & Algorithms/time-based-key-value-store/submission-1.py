class TimeMap:

    def __init__(self):
        self.hmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        data = (timestamp, value)
        self.hmap[key].append(data)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return "" 

        l, r = 0, len(self.hmap[key]) - 1
        res = ""
        while l <= r:
            mid = ((r - l) // 2) + l
            t, v = self.hmap[key][mid]
            if t <= timestamp:
                l = mid + 1
                res = v
            else:
                r = mid - 1

        return res
