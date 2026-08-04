class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        a = sum(nums)
        if a%2==1:
            return False
        a = a/2
        def dfs(i, rem):
            if rem==0:
                return True
            if i>=len(nums):
                return False
            a = nums[i]
            return dfs(i+1, rem-a) or dfs(i+1, rem)
        return dfs(0,a)


            
            

            

