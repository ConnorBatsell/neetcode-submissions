class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,sub):
            s = sum(sub)
            if i>=len(candidates) or s>=target:
                if s==target:
                    res.append(sub.copy())
                return
            sub.append(candidates[i])
            dfs(i+1, sub)
            sub.pop()
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            dfs(i+1, sub)
        dfs(0,[])
        return res
