class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            while q:
                a,b = q.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                
                for dr, dc in directions:
                    if ((a+dr) in range(row) and (b+dc) in range(col) and grid[a+dr][b+dc]=="1"):
                        grid[a+dr][b+dc]="0"
                        q.append((a+dr, b+dc))


        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1
        return islands

