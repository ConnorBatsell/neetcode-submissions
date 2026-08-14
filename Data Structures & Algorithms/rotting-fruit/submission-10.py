class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        rows,cols = len(grid), len(grid[0])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    rotten.append([r,c])

        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        mins = 0
        while rotten and fresh>0:
            for i in range(len(rotten)):
                r,c = rotten.popleft()
                for dr,dc in directions:
                    a,b = r+dr, c+dc
                    if min(a,b)<0 or a==rows or b==cols or grid[a][b]!=1:
                        continue
                    fresh-=1
                    rotten.append([a,b])
                    grid[a][b]=2
            mins+=1
        return mins if fresh==0 else -1








        
        