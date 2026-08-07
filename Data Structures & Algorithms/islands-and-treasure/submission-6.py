class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (2**31)-1
        rows = len(grid)
        cols = len(grid[0])
        dr = ((-1,0), (1,0), (0,-1), (0,1))
        def bfs(r,c):
            q = deque()
            q.append((r,c,0))
            while q:
                a,b,d = q.popleft()
                for x,y in dr:
                    if min(a+x,b+y)>=0 and a+x<rows and b+y<cols and d+1<grid[a+x][b+y]:
                        grid[a+x][b+y] = d+1
                        q.append((a+x,b+y, d+1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    bfs(r,c)
            


            

            

        