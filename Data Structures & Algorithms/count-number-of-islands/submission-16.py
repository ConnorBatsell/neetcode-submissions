class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])


        def bfs(r,c):
            q = deque()
            q.append((r,c))
            dr = ((-1,0), (1,0), (0,1), (0,-1))
            grid[r][c] = "0"
            while q:
                i,j = q.popleft()
                for a,b in dr:
                    if i+a>=0 and i+a<rows and j+b>=0 and j+b<cols:
                        if grid[i+a][j+b]=="1":
                            q.append(((i+a,j+b)))
                            grid[i+a][j+b] = "0"
                         
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    bfs(i,j)
                    res+=1
        return res
                
                


