class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax=1
        curMin=1
        ans=-10000
        for num in nums:
            a = num
            b = curMax*num
            c = curMin*num
            curMax = max(a,b,c)
            curMin = min(a,b,c)
            ans = max(ans, max(a,curMax,curMin))
        return ans
