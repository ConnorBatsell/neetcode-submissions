import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        while(len(heap)>1):
            a = heapq.heappop_max(heap)
            b = heapq.heappop_max(heap)
            heapq.heappush_max(heap, abs(a-b))
        return heapq.heappop(heap)
        