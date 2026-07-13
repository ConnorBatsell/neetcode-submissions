class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        k = r
        while l<=r:
            m = (l+r)//2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/m)
            if hours <= h:
                r=m-1
                k = min(k, m)
            else:
                l = m+1
        return k