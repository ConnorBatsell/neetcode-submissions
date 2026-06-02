class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r = sum(weights)
        res = r
        while l<=r:
            m = l + ((r-l)//2)
            count = 0
            temp = 0
            for weight in weights:
                temp += weight
                if temp > m:
                    count+=1
                    temp = weight
            while temp>m:
                count+=1
                temp = temp-m
            count+=1
            print(count)
            if count > days:
                l = m+1
            else:
                r = m-1
                res = m
                
        return res