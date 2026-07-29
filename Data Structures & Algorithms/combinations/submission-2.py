class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i,tmp):
            nonlocal k,n
            if len(tmp)==k or i>n:
                if len(tmp)==k:
                    res.append(tmp.copy())
                return
            for j in range(i,n+1):
                tmp.append(j)
                dfs(j+1,tmp)
                tmp.pop()
        dfs(1,[])
        return res
                