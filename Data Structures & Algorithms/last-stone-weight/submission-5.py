import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        while(len(heap)>1):
            a = heapq.heappop(heap)
            heapq.heapify_max(heap)
            b = heapq.heappop(heap)
            print(str(a) + ", " + str(b))
            heapq.heappush(heap, abs(a-b))
            heapq.heapify_max(heap)
        return heapq.heappop(heap)
        