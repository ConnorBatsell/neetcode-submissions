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
        intervals = sorted(intervals, key = lambda x:x.start)
        t = intervals[0]
        res = 0
        for i in range(1,len(intervals)):
            a = intervals[i]
            if a.start < t.end:
                return False
            else:
                t = a
        return True
        