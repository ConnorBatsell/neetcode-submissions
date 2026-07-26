class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] *n for _ in range(n)]
        cols = set()
        pos = set()
        neg = set()
        res = []
        def dfs(r):
            if r==n:
                temp = []
                for i in range(len(board)):
                    temp.append("".join(board[i]))
                res.append(temp)
                return
            for c in range(n):
                pDag = r+c
                nDag = r-c
                if pDag in pos or nDag in neg or c in cols:
                    continue
                board[r][c] = "Q"
                pos.add(pDag)
                neg.add(nDag)
                cols.add(c)
                dfs(r+1)
                cols.remove(c)
                neg.remove(nDag)
                pos.remove(pDag)
                board[r][c] = "."
        dfs(0)
        return res
