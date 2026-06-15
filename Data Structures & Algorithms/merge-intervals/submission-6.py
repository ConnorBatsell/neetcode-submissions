class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda y: y[0])
        temp = intervals[0]
        for i in range(1,len(intervals)):
            if temp[1] < intervals[i][0]:
                out.append(temp)
                temp = intervals[i]
            else:
                temp[1] = max(temp[1], intervals[i][1])
        out.append(temp)
        return out