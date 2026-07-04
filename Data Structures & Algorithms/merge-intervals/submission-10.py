class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        out = []
        t = intervals[0]
        for i in range(1, len(intervals)):
            a = intervals[i]
            if t[1] < a[0]:
                out.append(t)
                t = a
            else:
                t[0] = min(a[0], t[0])
                t[1] = max(a[1], t[1])
        out.append(t)
        return out
