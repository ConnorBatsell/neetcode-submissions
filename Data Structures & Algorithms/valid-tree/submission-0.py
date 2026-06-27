class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == n-1:
            return False
        
        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        q = deque([0])
        visit.add(0)
        while q:
            c = q.popleft()
            for ne in adj[c]:
                if ne not in visit:
                    visit.add(ne)
                    q.append(ne)
                    
        return len(visit)==n