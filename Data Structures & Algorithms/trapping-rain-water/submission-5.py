class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r = 0, len(height)-1
        maxL = height[l]
        maxR = height[r]
        res = 0
        while l<r:
            if maxL<maxR:
                l+=1
                res+= max(0,maxL-height[l])
                maxL = max(maxL, height[l])
                
            else:
                r-=1
                res+= max(0,maxR - height[r])
                maxR = max(maxR, height[r])
                
        return res 
            
        



