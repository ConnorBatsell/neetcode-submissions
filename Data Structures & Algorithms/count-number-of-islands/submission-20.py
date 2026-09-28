from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def bfs(r,c):
            s = deque()
            s.append((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            grid[r][c] = "0"
            while s:
                a,b = s.popleft()
                for dr,dc in directions:
                    x,y = a+dr, b+dc
                    if 0<=x<rows and 0<=y<cols and grid[x][y]=="1":
                        grid[x][y]="0"
                        s.append((x,y))

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    res+=1
                    bfs(r,c)
        return res

                    



                


