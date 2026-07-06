class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = 0
        for n in nums:
            curr = max(curr, 0)
            curr += n
            maxSum = max(maxSum, curr)
        return maxSum