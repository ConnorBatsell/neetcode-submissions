class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        output = []
        an = set()
        def dfs(course):
            if course in visit:
                return False
            if course in an:
                return True
            reqs = preMap[course]
            visit.add(course)
            for a in reqs:
                if dfs(a)==False:
                    return False
            visit.discard(course)
            an.add(course)
            output.append(course)
            return True
        out = []
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return output

            
        