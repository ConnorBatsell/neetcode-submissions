class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        for i in range(len(intervals)):
            a = intervals[i]
            if newInterval[1] < a[0]:
                out.append(newInterval)
                return out + intervals[i:]
            elif newInterval[0]>a[1]:
                out.append(a)
            else:
                newInterval[0] = min(newInterval[0], a[0])
                newInterval[1] = max(newInterval[1], a[1])
        out.append(newInterval)
        return out