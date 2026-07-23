class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, sub):
            s = sum(sub)
            if i>=len(nums) or s>=target:
                if s==target:
                    res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i, sub)
            sub.pop()
            dfs(i+1, sub)
        dfs(0,[])
        return res