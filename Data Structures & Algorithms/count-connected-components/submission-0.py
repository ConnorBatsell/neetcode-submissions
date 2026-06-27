class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()
        def dfs(i):
            visit.add(i)
            for nei in adj[i]:
                if nei not in visit:
                    dfs(nei)
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count+=1
        return count
            
            
