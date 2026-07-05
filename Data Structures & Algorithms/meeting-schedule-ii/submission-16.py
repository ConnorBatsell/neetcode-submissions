"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x:x.start)
        out = 1
        if not intervals:
            return 0
        h = []
        for n in intervals:
            if h and h[0] <= n.start:
                heapq.heappop(h)
            heapq.heappush(h, n.end)
        return len(h)