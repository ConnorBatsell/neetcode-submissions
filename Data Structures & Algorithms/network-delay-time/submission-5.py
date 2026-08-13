class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        for t in times:
            adj[t[0]].append([t[2], t[1]])
        minH = [(0,k)]
        visit = set()
        res = 0
        while minH:
            t,s = heapq.heappop(minH)
            if s in visit:
                continue
            visit.add(s)
            res = max(res,t)
            for t2,s2 in adj[s]:
                heapq.heappush(minH, [t+t2,s2])
        for i in range(1,n+1):
            if i not in visit:
                return -1
        return res



