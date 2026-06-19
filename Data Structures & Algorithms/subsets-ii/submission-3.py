class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sub = []
        def dfs(i):
            if i>=len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i+1)
            a = sub.pop()
            increment = 1
            while i+increment<len(nums) and nums[i+increment]==a:
                increment+=1
            dfs(i+increment)
        dfs(0)
        return res
        