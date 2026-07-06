class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g = len(nums)-1
        for i in range(g, -1, -1):
            if i+nums[i]>=g:
                g = i
        return True if g==0 else False        
