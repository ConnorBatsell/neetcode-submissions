class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = defaultdict(list)
        for a,b in prerequisites:
            preReq[a].append(b)
        visit = set()
        def dfs(i):
            if preReq[i]==[]:
                return True
            if i in visit:
                return False
            visit.add(i)
            for j in preReq[i]:
                if not dfs(j):
                    return False
            visit.discard(i)
            preReq[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True







            



