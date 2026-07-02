class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        output=0
        
        def bfs(r,c, grid):
            q = deque()
            q.append([r,c])
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                a,b = q.popleft()
                for dr,dc in directions:
                    nr,nc = a+dr,b+dc
                    if min(nr,nc)<0 or nr==rows or nc==cols or grid[nr][nc]=="0":
                        continue
                    q.append([nr,nc])
                    grid[nr][nc] = "0"


            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    bfs(i,j, grid)
                    output+=1

        return output                


