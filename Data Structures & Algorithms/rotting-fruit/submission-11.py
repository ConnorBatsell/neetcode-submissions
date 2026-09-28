from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        mins = 0
        while rotten and fresh>0:
            for i in range(len(rotten)):
                r,c = rotten.popleft()
                for dr, dc in directions:
                    x,y = r+dr, c+dc
                    if 0<=x<rows and 0<=y<cols and grid[x][y]==1:
                        grid[x][y] = 2
                        rotten.append((x,y))
                        fresh-=1
            mins+=1
        return mins if fresh==0 else -1
                    

        








        
        