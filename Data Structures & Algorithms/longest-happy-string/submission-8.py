class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = {}
        if a==0 and b==0 and c==0:
            return ""
        counts['a'] = a
        counts['b'] = b
        counts['c'] = c
        heap = []
        for key,val in counts.items():
            if val >0:
                heapq.heappush(heap, [-val, key])
        res = []
        while heap:
            a = heapq.heappop(heap)
            if len(res)>=2 and res[-1]==a[1] and res[-2]==a[1]:
                if heap:
                    b = heapq.heappop(heap)
                    res.append(b[1])
                    if b[0]+1<0:
                        heapq.heappush(heap, [b[0]+1, b[1]])
                    heapq.heappush(heap, [a[0], a[1]])
                else:
                    break
            else:
                res.append(a[1])
                if a[0]+1<0:
                    heapq.heappush(heap, [a[0]+1, a[1]])
        return "".join(res)


        
            

