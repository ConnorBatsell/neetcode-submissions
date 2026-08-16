class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        r = defaultdict(list)
        for a,b in prerequisites:
            r[a].append(b)
        visit = set()
        def dfs(i):
            if i in visit:
                return False
            if r[i]==[]:
                return True
            visit.add(i)
            for a in r[i]:
                if not dfs(a):
                    return False
            visit.discard(i)
            r[i] = []
            return True
                
        for j in range(numCourses):
            if not dfs(j):
                return False
        return True




            



