class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = max(nums)
        for i in range(0, len(nums)):
            l,r=i-1,i+1
            curr = nums[i]
            while l>=0 and r<len(nums):
                curr *= nums[l]
                m = max(m, curr)
                curr *= nums[r]
                m = max(m, curr)
                l-=1
                r+=1
            l,r=i,i+1
            curr = 1
            while l>=0 and r<len(nums):
                curr *= nums[l]
                m = max(m, curr)
                curr *= nums[r]
                m = max(m, curr)
                l-=1
                r+=1
            
        return m