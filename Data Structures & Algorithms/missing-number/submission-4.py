class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(0,len(nums)):
            res |= 1<<nums[i]
        a = (1<<len(nums)+1) - 1
        diff = res^a
        for j in range(0,32):
            t = 1<<j
            if t&diff:
                return j
