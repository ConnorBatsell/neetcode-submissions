class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r = 0,len(height)-1
        maxL = height[l]
        maxR = height[r]
        res = 0
        while l<r:
            if maxL < maxR:
                l+=1
                res += max(maxL-height[l], 0)
                maxL = max(maxL, height[l])
                
            else:
                r-=1
                res += max(maxR-height[r], 0)
                maxR = max(maxR, height[r])
                
        return res
            
        



