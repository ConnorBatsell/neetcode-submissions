from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)
        if len(nums)==1:
            return nums[0]
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cache[i] = max(cache[i-1], nums[i]+cache[i-2])
        return cache[len(nums)-1]
            