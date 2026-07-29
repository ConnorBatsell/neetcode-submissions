class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i,tmp):
            nonlocal k,n
            if len(tmp)==k or i>n:
                if len(tmp)==k:
                    res.append(tmp.copy())
                return
            tmp.append(i)
            dfs(i+1,tmp)
            tmp.pop()
            dfs(i+1,tmp)
            return
        dfs(1,[])
        return res
                