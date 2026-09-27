"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key = lambda i: i.start)
        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if ((intervals[i].start < end and intervals[i].start >= start) or 
                (intervals[i].end <= end and intervals[i].end > start) or 
                (intervals[i].start <= start and intervals[i].end >= end)):
                return False
            start = intervals[i].start
            end = intervals[i].end
        return True

