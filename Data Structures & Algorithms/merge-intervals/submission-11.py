class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        out = []
        t = intervals[0]
        for i in range(1,len(intervals)):
            x = intervals[i]
            if t[1]<x[0]:
                out.append(t)
                t = x
            else:
                t[1] = max(x[1],t[1])
        out.append(t)
        return out
