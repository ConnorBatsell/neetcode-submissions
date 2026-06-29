class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = x
        if n > 0:
            while n>1:
                p *= x
                n-=1
            return p
        else:
            if n==0:
                return 1
            n=abs(n)
            p=1/x
            while n>1:
                p*=1/x
                n-=1
            return p