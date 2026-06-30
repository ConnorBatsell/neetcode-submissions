class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        
        for u,v,t in times:
            adj[u].append((t,v))
        
        shortest = {}
        minHeap = [(0,k)]
        while minHeap:
            t,v = heapq.heappop(minHeap)
            if v in shortest:
                continue
            shortest[v] = t
            
            for a,b in adj[v]:
                if b not in shortest:
                    heapq.heappush(minHeap, (a+t,b))
        for i in range(1,n+1):
            if not i in shortest:
                return -1
        return max(shortest.values())