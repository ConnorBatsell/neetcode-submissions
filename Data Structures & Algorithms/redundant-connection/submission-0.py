class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i:[] for i in range(1,n+1)}
        

        def dfs(u, v, visited):
            if u==v:
                return True
            visited.add(u)
            for nei in adj[u]:
                if nei not in visited:
                    if dfs(nei,v,visited):
                        return True
            return False
        for u,v in edges:
            if dfs(u,v,set()):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)
            