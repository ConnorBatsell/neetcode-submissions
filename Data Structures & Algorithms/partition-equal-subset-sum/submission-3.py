class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2==1:
            return False
        s = s//2
        n = len(nums)
        cache = [[False] * (s+1) for _ in range(n+1)]
        for i in range(n+1):
            cache[i][0] = True
        for i in range(1,n+1):
            for j in range(1,s+1):
                if nums[i-1]<=j:
                    cache[i][j] = (cache[i-1][j]) or cache[i-1][j-nums[i-1]]
                else:
                    cache[i][j] = cache[i-1][j]
        return cache[n][s]
            

        # def dfs(i,rem):
        #     if rem==0:
        #         return True
        #     if i>=n:
        #         return False
        #     cache[i][rem] = dfs(i+1, rem-nums[i]) or dfs(i+1, rem)
        #     return cache[i][rem]
        # return dfs(0,s)


            
            

            

