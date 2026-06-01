class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x+1
        res=0
        while l<r:
            m = (l+r)//2
            if m*m==x:
                return m
            elif m*m < x:
                l=m+1
                res=m
            else:
                r=m
        return res

            