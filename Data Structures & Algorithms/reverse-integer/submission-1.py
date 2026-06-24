class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        count = 0
        neg = x<0
        x=abs(x)
        while x>0:
            tmp = x%10
            x = x//10
            n*=10
            n+=tmp
        if neg:
            n*=-1
        if not (-2**31) <= n <= ((2**31)-1):
            return 0
        return n