class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
            while len(heap)>len(nums)-k+1:
                heapq.heappop(heap)
        return -heap[0]

            