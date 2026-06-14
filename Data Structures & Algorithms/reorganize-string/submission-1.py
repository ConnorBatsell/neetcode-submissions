class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c]+=1
        heap = []
        for key,val in counts.items():
            if val > (len(s)+1)//2:
                return ""
            heapq.heappush(heap, [-val, key])
        temp = []
        res = ""
        while heap:
            a = heapq.heappop(heap)
            a[0]+=1
            res += a[1]
            if temp and temp[0]<0:
                heapq.heappush(heap, temp)
            temp = a
        return res


        