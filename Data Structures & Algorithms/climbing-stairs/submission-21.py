class Solution:
    def climbStairs(self, n: int) -> int:
        cache=[0]*(n+1)
        cache[1] = 1
        cache[0] = 1
        for i in range(2,n+1):
            cache[i] = cache[i-2] + cache[i-1]
        return cache[n]
        

        