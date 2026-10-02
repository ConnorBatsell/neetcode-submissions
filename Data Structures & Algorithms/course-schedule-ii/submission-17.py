class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = defaultdict(list)
        for a,b in prerequisites:
            preReq[a].append(b)
        visit = set()
        out = []
        def dfs(i):
            if preReq[i]==[]:
                if not i in out:
                    out.append(i)
                return True
            if i in visit:
                return False
            visit.add(i)
            for j in preReq[i]:
                if not dfs(j):
                    return False
            visit.discard(i)
            preReq[i] = []
            out.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return out
        