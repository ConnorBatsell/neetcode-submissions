class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        ma, mi = 1,1
        for i in range(len(nums)):
            num = nums[i]
            tmp = ma*num
            ma = max(tmp, mi*num, num)
            mi = min(tmp, mi*num, num)
            res = max(res, ma)
        return res
