class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        res = [intervals[0]]
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= end:
                res[-1][1] = max(end, e)
                start, end = s, max(end, e)
            else:
                res.append([s, e])
                start, end = s, e 
 
        return res
            

