class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}

        def dfs(i, t):
            if (i,t) in cache:
                return cache[(i,t)]
            if i==len(nums):
                return 1 if t==target else 0
            ad = dfs(i+1, t+nums[i])
            sub = dfs(i+1, t-nums[i])
            cache[(i,t)] = ad+sub
            return cache[(i,t)]
        
        return dfs(0,0)
            