from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (2**31) - 1
        rows = len(grid)
        cols = len(grid[0])
        dst = 0
        s = deque()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    s.append((r,c))
        while s:
            a,b = s.popleft()
            for dr, dc in directions:
                x,y = a+dr, b+dc
                if 0<=x<rows and 0<=y<cols and grid[x][y]==INF:
                    grid[x][y] = grid[a][b] + 1
                    s.append((x,y))
        




        
            


            

            

        