class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        if a==0 and b==0 and c==0:
            return ""
        heapq.heappush(h, (-a, "a"))
        heapq.heappush(h, (-b, "b"))
        heapq.heappush(h, (-c, "c"))
        res = ""
        while h:
            a = heapq.heappop(h)
            if a[0]<0:
                if len(res)>=2 and res[-1]==a[1] and res[-2]==a[1]:
                    if h:
                        b = heapq.heappop(h)
                        if b[0]<0:
                            res += b[1]
                            heapq.heappush(h, (b[0]+1, b[1]))
                            heapq.heappush(h, (a[0], a[1]))
                        else:
                            break
                    else:
                        break
                else:
                    res += a[1]
                    if a[0]+1<0:
                        heapq.heappush(h, (a[0]+1, a[1]))
            else:
                break
        return res




        
            

