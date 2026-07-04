class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        for i in range(len(intervals)):
            temp = intervals[i]
            if newInterval[1] < temp[0]:
                out.append(newInterval)
                return out + intervals[i:]
            elif newInterval[0] > temp[1]:
                out.append(temp)
            else:
                newInterval[0] = min(newInterval[0], temp[0])
                newInterval[1] = max(newInterval[1], temp[1])
        out.append(newInterval)
        return out