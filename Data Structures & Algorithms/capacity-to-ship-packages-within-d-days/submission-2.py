class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l<=r:
            m = l + ((r-l)//2)
            count = 1
            temp = 0
            for weight in weights:
                if temp + weight > m:
                    count += 1
                    temp = weight
                else:
                    temp += weight
            if count > days:
                l = m+1
            else:
                r = m-1
                res = m
                
        return res