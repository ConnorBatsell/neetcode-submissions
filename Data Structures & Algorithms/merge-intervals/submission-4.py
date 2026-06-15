class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        temp = intervals[0]
        for i in range(1,len(intervals)):
            if temp[1] < intervals[i][0]:
                out.append(temp)
                temp = intervals[i]
            else:
                temp[0] = min(temp[0], intervals[i][0])
                temp[1] = max(temp[1], intervals[i][1])
        out.append(temp)
        return out