class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = len(nums)-1
        for i in range(a, -1, -1):
            if i+nums[i]>=a:
                a=i
        return True if a==0 else False

