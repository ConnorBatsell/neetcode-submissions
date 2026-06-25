class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(grid, r, c, visit):
            if (min(r,c)<0 or r==rows or c==cols or (r,c) in visit or grid[r][c]==0):
                return 0
            grid[r][c]=0
            visit.add((r,c))
            area = 1
            area += dfs(grid,r+1,c,visit)
            area += dfs(grid,r-1,c,visit)
            area += dfs(grid,r,c+1,visit)
            area += dfs(grid,r,c-1,visit)
            visit.remove((r,c))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    m = max(m,dfs(grid, r,c, set()))
        return m
