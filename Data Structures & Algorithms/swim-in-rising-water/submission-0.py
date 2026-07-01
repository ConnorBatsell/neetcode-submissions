class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(grid)
        visit = set()
        directions=[[-1,0], [1,0], [0,1], [0,-1]]
        #time/max-height, r, c
        minH = [[grid[0][0], 0, 0]]
        visit.add((0,0))
        while minH:
            t,r,c = heapq.heappop(minH)
            if r==n-1 and c==n-1:
                return t
            for dr,dc in directions:
                if min(r+dr, c+dc)<0 or r+dr==n or c+dc==n or(r+dr,c+dc) in visit:
                    continue
                visit.add((r+dr, c+dc))
                heapq.heappush(minH, [max(t, grid[r+dr][c+dc]), r+dr, c+dc])
            

