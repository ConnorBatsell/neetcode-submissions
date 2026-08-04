class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        out = r
        while l<=r:
            m = (l+r)//2
            temp = 0
            for pile in piles:
                temp+=math.ceil(pile/m)
            if temp <= h:
                out = min(out, m)
                r=m-1
            else:
                l=m+1
        return out
