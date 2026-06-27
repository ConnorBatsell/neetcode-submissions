class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        output=0
        visit = set()
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                r,c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    a,b = r+dr, c+dc
                    if (min(a,b)<0 or a==rows or b==cols or (a,b) in visit or grid[a][b]=="0"):
                        continue
                    q.append((a,b))
                    visit.add((a,b))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    output+=1
                
        return output


