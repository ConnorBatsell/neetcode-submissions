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
        intervals = sorted(intervals, key=lambda x:x.start)
        temp = intervals[0]
        for i in range(1,len(intervals)):
            if temp.end > intervals[i].start:
                return False
            temp = intervals[i]
        return True
        