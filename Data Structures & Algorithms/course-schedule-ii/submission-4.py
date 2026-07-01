class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        out = []
        ans = set()
        def dfs(c):
            if c in visit:
                return False
            if c in ans:
                return True
            visit.add(c)
            for crs in preMap[c]:
                if not dfs(crs):
                    return False
            visit.remove(c)
            ans.add(c)
            out.append(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return out

            
        