class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()
        def bfs(r,c):
            if min(r,c)<0 or r==rows or c==cols or grid[r][c]==-1 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append([r,c])
            return
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append([i,j])
                    visit.add((i,j))
        depth = 0
        while q:
            for i in range(len(q)):
                a,b = q.popleft()
                grid[a][b] = depth
                bfs(a+1, b)
                bfs(a-1, b)
                bfs(a,b+1)
                bfs(a,b-1)
            depth+=1
        