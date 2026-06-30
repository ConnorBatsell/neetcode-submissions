class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for src,dest in tickets:
            adj[src].append(dest)
        path = ["JFK"]
        def dfs(src):
            if len(path)==len(tickets)+1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i,v in enumerate(temp):
                adj[src].pop(i)
                path.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i,v)
                path.pop()
            return False
        dfs("JFK")
        return path

