"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x: x.start)
        out = 1
        if not intervals:
            return 0
        heap = []
        for n in intervals:
            if heap and heap[0] <= n.start:
                heapq.heappop(heap)
            heapq.heappush(heap, n.end)
        return len(heap)