class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time,fresh = 0,0
        rows,cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        # while rotten
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    a,b = r+dr, c+dc
                    if min(a,b)<0 or a==rows or b==cols or grid[a][b]!=1:
                        continue
                    fresh-=1
                    grid[a][b]=2
                    q.append([a,b])

            time+=1
        return time if fresh==0 else -1
                    




        
        