class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        for ui,vi,ti in times:
            adj[ui].append((vi,ti))
        shortest = {}
        minHeap = [(0,k)]
        while minHeap:
            ti,vi = heapq.heappop(minHeap)
            if vi in shortest:
                continue
            shortest[vi] = ti
            for va,ta in adj[vi]:
                if not va in shortest:
                    heapq.heappush(minHeap, (ta+ti,va))
        for i in range(1,n+1):
            if not i in shortest:
                return -1
        return max(shortest.values())
    


        
