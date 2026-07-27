class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n<=2:
            if n==1:
                return nums[0]
            return max(nums[0],nums[1])
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        res = 0
        for i in range(2,len(nums)-1):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        res = dp[len(nums)-2]
        dp = [0]*len(nums)
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        res = max(res, dp[len(nums)-1])
        return res
            
        