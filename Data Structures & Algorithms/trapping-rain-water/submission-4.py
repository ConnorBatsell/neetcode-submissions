class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        left = height[0]
        right = height[len(height)-1]
        for i in range(len(height)):
            left = max(left, height[i])
            maxLeft[i] = left
            right = max(right, height[len(height)-(i+1)])
            maxRight[len(height)-(i+1)] = right
        minHeights = [0]*len(height)
        for i in range(len(height)):
            minHeights[i] = min(maxLeft[i], maxRight[i])
        res = 0
        for i in range(len(height)):
            res+=max(0,minHeights[i]-height[i])
        return res
            
        



