class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        r = defaultdict(list)
        for a,b in prerequisites:
            r[a].append(b)
        visit = set()
        out = []
        def dfs(i):
            if i in visit:
                return False
            if r[i] is None:
                return True
            visit.add(i)
            for a in r[i]:
                if not dfs(a):
                    return False
            visit.discard(i)
            r[i] = None
            out.append(i)
            return True
                
        for j in range(numCourses):
            if not dfs(j):
                return []
        return out