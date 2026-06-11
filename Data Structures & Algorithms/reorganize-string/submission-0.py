class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c]+=1
        heap = []
        for key,value in counts.items():
            if value > (len(s)+1)//2:
                return ""
            else:
                heapq.heappush(heap, [-value, key])
        out = ""
        temp = []
        while heap:
            a = heapq.heappop(heap)
            a[0] += 1
            out += a[1]
            if temp and temp[0] <0:
                heapq.heappush(heap, temp)
            temp = a

        return out
       

        