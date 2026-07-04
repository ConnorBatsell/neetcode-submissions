class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        t = intervals[0][1]
        res = 0
        for i in range(1,len(intervals)):
            a = intervals[i]
            if t > a[0]:
                res +=1
                t = min(t, a[1])
            else:
                t=a[1]
        return res

