class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            dire = [[-1,0],[1,0],[0,1],[0,-1]]
            grid[r][c] = '0'
            while q:
                a,b = q.popleft()
                for dr,dc in dire:
                    if 0<=a+dr<rows and 0<=b+dc<cols and grid[a+dr][b+dc]=='1':
                        grid[a+dr][b+dc] = '0'
                        q.append((a+dr,b+dc))
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    bfs(r,c)
                    res+=1
        return res
                    



                


