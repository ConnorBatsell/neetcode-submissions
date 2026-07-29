class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."]*n for i in range(n)]
        cols = set()
        pDag = set()
        nDag = set()
        self.res = 0
        def dfs(r):
            nonlocal n
            if r==n:
                self.res += 1
                return
            for c in range(n):
                p = r+c
                neg = r-c
                if p in pDag or neg in nDag or c in cols:
                    continue
                pDag.add(p)
                nDag.add(neg)
                cols.add(c)
                dfs(r+1)
                pDag.remove(p)
                nDag.remove(neg)
                cols.remove(c)
        dfs(0)
        return self.res
                
