class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        def dfs(r,c,visit,prevHeight):
            if min(r,c)<0 or r==rows or c==cols or (r,c) in visit or heights[r][c]<prevHeight:
                return
            prevHeight = heights[r][c]
            visit.add((r,c))
            dfs(r+1,c, visit, prevHeight)
            dfs(r-1,c, visit, prevHeight)
            dfs(r,c+1, visit, prevHeight)
            dfs(r,c-1, visit, prevHeight)
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        res = []
        for idx, val in enumerate(pac):
            if val in atl:
                res.append(val)
        return res


