class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def dfs(i, sub):
            s = sum(sub)
            if s==target:
                res.append(sub.copy())
                return
            if s>target or i>=len(candidates):
                return 
            sub.append(candidates[i])
            dfs(i+1, sub)
            sub.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,sub)
        dfs(0,[])
        return res