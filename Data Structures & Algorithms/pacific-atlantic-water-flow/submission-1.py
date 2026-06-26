class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        def dfs(r,c, visit, prevHeight):
            if ((r,c) in visit or min(r,c)<0 or r==rows or c==cols or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
        for r in range(rows):
            dfs(r,0,pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl, heights[rows-1][c])
        out = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    out.append([r,c])
        return out
