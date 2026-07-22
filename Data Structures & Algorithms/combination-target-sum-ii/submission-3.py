class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, sub):
            s = sum(sub)
            if s>=target or i>=len(candidates):
                if s==target:
                    res.append(sub.copy())
                return
            sub.append(candidates[i])
            dfs(i+1, sub)
            sub.pop()
            while i<len(candidates)-1 and candidates[i+1]==candidates[i]:
                i+=1
            dfs(i+1, sub)
        dfs(0,[])
        return res