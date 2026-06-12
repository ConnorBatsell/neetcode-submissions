class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = {}
        if a==0 and b==0 and c==0:
            return ""
        counts['a'] = a
        counts['b'] = b
        counts['c'] = c
        heap = []
        for key,count in counts.items():
            if count>0:
                heapq.heappush(heap, [-count, key])
        out = []
        while heap:
            val, key = heapq.heappop(heap)
            if len(out)>=2 and out[-1]==key and out[-2]==key:
                if heap:
                    val2, key2 = heapq.heappop(heap)
                    out.append(key2)
                    if val2+1<0:
                        heapq.heappush(heap, [val2+1, key2])
                    heapq.heappush(heap, [val, key])
                else:
                    break
            else:
                out.append(key)
                if val+1<0:
                    heapq.heappush(heap, [val+1, key])
        
        return "".join(out)
            

