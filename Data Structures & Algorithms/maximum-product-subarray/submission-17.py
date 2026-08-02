class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax,curMin = 1,1
        for i in range(len(nums)):
            temp = curMax*nums[i]
            curMax = max(nums[i], curMax*nums[i], curMin*nums[i])
            curMin = min(temp, nums[i], curMin*nums[i])
            res = max(res,curMax)
        return res

