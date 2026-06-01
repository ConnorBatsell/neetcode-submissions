class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l<r:
            m = (l+r)//2
            if m*m==x:
                return m
            elif m*m < x:
                l=m+1
            else:
                r=m
        if x==0:
            return 0
        elif x==1:
            return 1
        return l-1
            