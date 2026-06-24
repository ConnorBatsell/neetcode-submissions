class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = 0
        for i in range(0,len(nums)+1):
            if not curr in nums:
                return curr
            curr+=1
        