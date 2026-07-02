class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        for u,v,t in times:
            adj[u].append([t,v])
        minH = [(0,k)]
        visit = set()
        time = 0
        while minH:
            t,v = heapq.heappop(minH)
            if v in visit:
                continue
            visit.add(v)
            time = t
            for ti,vi in adj[v]:
                if not vi in visit:
                    heapq.heappush(minH, [t + ti,vi])
        for i in range(1,n+1):
            if not i in visit:
                return -1
        return time 
    


        
