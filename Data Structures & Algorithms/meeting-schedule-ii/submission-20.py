"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key = lambda x:x.start)
        h = []
        if not intervals:
            return 0
        for i in range(len(intervals)):
            t = intervals[i]
            if h and h[0] <= t.start:
                heapq.heappop(h)
            heapq.heappush(h, t.end)
        return len(h)

