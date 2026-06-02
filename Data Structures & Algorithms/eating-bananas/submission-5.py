class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r = max(piles)
        mi = r
        while l<=r:
            m = l + ((r-l)//2)
            count = 0
            for pile in piles:
                count += math.ceil(float(pile)/m)
            if count > h:
                l=m+1
            else:
                r=m-1
                mi = m
        return mi