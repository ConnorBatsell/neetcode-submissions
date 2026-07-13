class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while s and s[-1][1]>h:
                a,b = s.pop()
                maxArea = max(maxArea, b * (i-a))
                start = a
            s.append([start,h])
        for i,h in s:
            maxArea = max(maxArea, h * (len(heights)-i))
        return maxArea


