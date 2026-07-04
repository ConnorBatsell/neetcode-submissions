class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        prof = []
        minC = [(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(minC)
        for i in range(k):
            while minC and minC[0][0]<=w:
                a,b = heapq.heappop(minC)
                heapq.heappush(prof, -b)
            if not prof:
                break
            w += -heapq.heappop(prof)
        return w