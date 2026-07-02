class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}

        def dfs(i, t):
            if i==len(nums):
                if t==target:
                    return 1
                return 0
            if (i,t) in cache:
                return cache[(i,t)]
            ad = dfs(i+1, t+nums[i])
            sub = dfs(i+1, t-nums[i])
            cache[(i,t)] = ad+sub
            return cache[(i,t)]
        
        return dfs(0,0)
            