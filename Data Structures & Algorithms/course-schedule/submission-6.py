class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        def dfs(c):
            if c in visit:
                return False
            if preMap[c]==[]:
                return True
            visit.add(c)
            for crs in preMap[c]:
                if not dfs(crs):
                    return False
            visit.remove(c)
            
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


            



