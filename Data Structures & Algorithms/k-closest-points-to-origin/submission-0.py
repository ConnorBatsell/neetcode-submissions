class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        out = []
        for point in points:
            distance = ((point[0])**2 + (point[1])**2)
            heapq.heappush_max(heap, (distance, point))
            if len(heap)>k:
                heapq.heappop_max(heap)
        return [point for dist, point in heap]

                
