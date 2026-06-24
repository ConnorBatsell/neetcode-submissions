class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count= 0
        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if min(r,c)<0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c]=="0":
                return grid
            
            visit.add((r,c))
            grid[r][c]="0"
            dfs(grid, r+1, c, visit)
            dfs(grid, r-1, c, visit)
            dfs(grid, r, c+1, visit)
            dfs(grid, r, c-1, visit)
            visit.remove((r,c))
            return grid
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]=="1":
                    grid = dfs(grid, i, j, set())
                    print(grid)
                    count+=1
        return count

