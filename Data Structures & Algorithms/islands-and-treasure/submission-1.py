class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647   # the "empty land" sentinel in this problem

        def dfs(r, c, dist):
            # out of bounds, or a wall
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == -1:
                return
            # prune: someone already reached this cell as cheaply or cheaper
            if dist > grid[r][c]:
                return
            grid[r][c] = dist          # record the better distance
            dfs(r+1, c, dist+1)
            dfs(r-1, c, dist+1)
            dfs(r, c+1, dist+1)
            dfs(r, c-1, dist+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:    # start a DFS from each treasure
                    dfs(r, c, 0)