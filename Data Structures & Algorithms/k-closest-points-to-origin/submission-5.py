class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(heap,(-dist, x, y))
            if len(heap)>k:
                heapq.heappop(heap)
        out = []
        while heap:
            a = heapq.heappop(heap)
            out.append([a[1],a[2]])
        return out

                
