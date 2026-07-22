class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, sub):
            s = sum(sub)
            if s==target:
                res.append(sub.copy())
                return
            if s>target or i>=len(nums):
                return
            subset.append(nums[i])
            dfs(i, subset)
            subset.pop()
            dfs(i+1, subset)
        dfs(0,[])
        return res
            