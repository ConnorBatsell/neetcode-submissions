class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        def helper(r,c,cache):
            if r==m or c==n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r==m-1 and c==n-1:
                return 1

            cache[r][c] = helper(r+1,c,cache) + helper(r,c+1,cache)
            return cache[r][c]
        cache = [[0] * n for i in range(m)]
        return helper(0,0, cache)