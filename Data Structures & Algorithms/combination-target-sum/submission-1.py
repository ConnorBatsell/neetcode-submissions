class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i):
            a = sum(sub)
            if a>=target or i>=len(nums):
                if a==target:
                    res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i)
            sub.pop()
            dfs(i+1)
        dfs(0)
        return res
            