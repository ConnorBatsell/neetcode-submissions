class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        heap = []
        for key,val in counts.items():
            heapq.heappush(heap, (-val, key))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
