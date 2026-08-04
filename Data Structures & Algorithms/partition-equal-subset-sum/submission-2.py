class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2==1:
            return False
        s = s//2
        n = len(nums)
        cache = [[-1] * (s+1) for _ in range(n+1)]
        def dfs(i,rem):
            if rem==0:
                return True
            if i>=n:
                return False
            cache[i][rem] = dfs(i+1, rem-nums[i]) or dfs(i+1, rem)
            return cache[i][rem]
        return dfs(0,s)


            
            

            

