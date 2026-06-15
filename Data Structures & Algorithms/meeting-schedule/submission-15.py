"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals = sorted(intervals, key=lambda obj: obj.start)
        for i in range(1, len(intervals)):
            prev = intervals[i-1].end
            start = intervals[i].start
            if start < prev:
                return False
        return True