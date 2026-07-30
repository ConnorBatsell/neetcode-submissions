class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        cache = [[-1]*2 for _ in range(len(nums))]

        def dfs(i, f):
            if i>=len(nums) or (f and i==len(nums)-1):
                return 0
            if cache[i][f]!=-1:
                return cache[i][f]
            cache[i][f] = max(dfs(i+1, f), nums[i]+dfs(i+2, f))
            return cache[i][f]
        return max(dfs(0,True), dfs(1,False))



        
            
        