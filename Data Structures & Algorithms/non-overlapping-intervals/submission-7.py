class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        prev = intervals[0]
        res = []
        count = 0
        for i in range(1, len(intervals)):
            lastEnd = prev[1]
            if intervals[i][0]<lastEnd:
                count=count+1
                if lastEnd > intervals[i][1]:
                    prev = intervals[i]
                    res.append(intervals[i])
                else:
                    res.append(prev)
            else:
                prev = intervals[i]
                res.append(intervals[i])
        return count
