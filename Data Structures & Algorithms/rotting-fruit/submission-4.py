class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = -1
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        def ad(r,c):
            if(r<0 or r==rows or c<0 or c==cols or 
            (r,c) in visit or grid[r][c]==0):
                return 
            visit.add((r,c))
            q.append([r,c])
        fruitCount = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append([r,c])
                    visit.add((r,c))
                    fruitCount+=1
                elif grid[r][c]==1:
                    fruitCount+=1
        popCount = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                popCount+=1
                ad(r+1, c)
                ad(r-1, c)
                ad(r, c+1)
                ad(r, c-1)
            time+=1
        if fruitCount==0:
            return 0
        return time if fruitCount==popCount else -1
        