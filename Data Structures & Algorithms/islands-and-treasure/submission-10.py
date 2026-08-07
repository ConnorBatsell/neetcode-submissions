class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (2**31)-1
        rows = len(grid)
        cols = len(grid[0])
        dr = ((-1,0), (1,0), (0,-1), (0,1))
        visit = set()
        q = deque()
        def bfs(r,c):
            if (min(r,c)<0 or r==rows or c==cols or (r,c) in visit or grid[r][c]==-1):
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            dist+=1
            
            


            

            

        