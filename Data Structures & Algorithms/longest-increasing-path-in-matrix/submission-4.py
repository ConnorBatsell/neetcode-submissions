class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        rows = len(matrix)
        cols = len(matrix[0])
        def dfs(r,c,prev):
            if min(r,c) < 0 or r==rows or c==cols or matrix[r][c] <= prev:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            curr = matrix[r][c]
            dp[(r,c)] = 1 + max(dfs(r+1,c,curr), dfs(r-1,c,curr), dfs(r,c+1,curr), dfs(r,c-1,curr))
            return dp[(r,c)]
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res,dfs(i,j,float("-inf")))
        return res
