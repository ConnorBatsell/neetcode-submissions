class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h = []
        new = sorted(trips, key=lambda x:x[1])
        curr = 0
        for trip in new:
            while h and h[0][0]<=trip[1]:
                a,b = heapq.heappop(h)
                curr -= b
            if curr+trip[0]>capacity:
                return False
            heapq.heappush(h, (trip[2], trip[0]))
            curr += trip[0]
        return True
            
