class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev = nums[0]
        for num in nums:
            if num <prev:
                return num
            prev = num
        return nums[0]