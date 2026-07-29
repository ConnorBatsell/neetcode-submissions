class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        cache=[0]*(n+1)
        cache[1] = 1
        cache[2] = 2
        for i in range(3,n+1):
            cache[i] = cache[i-2] + cache[i-1]
        return cache[n]
        

        