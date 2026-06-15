class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        prev = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0]<prev:
                count=count+1
                if prev > intervals[i][1]:
                    prev = intervals[i][1]

                else:
                    continue
            else:
                prev = intervals[i][1]
        return count
