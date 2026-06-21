class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        ways1 = 1
        ways0 = 1
        for i in range(2, n+1):
            curr = ways1 + ways0
            temp = ways1
            ways1 = curr
            ways0 = temp
        return ways1
        