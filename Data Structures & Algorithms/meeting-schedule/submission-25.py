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
        e = 0
        intervals = sorted(intervals, key=lambda x:x.start)

        for i in range(len(intervals)):
            interval = intervals[i]
            if interval.start<e:
                return False
            e = interval.end
        return True
        