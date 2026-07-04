class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        prof = []
        minCap = [(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(minCap)
        for i in range(k):
            while minCap and minCap[0][0]<=w:
                x,y = heapq.heappop(minCap)
                heapq.heappush(prof, -y)
            if not prof:
                break
            w += -heapq.heappop(prof)
        return w