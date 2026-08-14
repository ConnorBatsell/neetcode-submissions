class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for a,b in prerequisites:
            pre[a].append(b)
        def dfs(i,visited):
            if i in visited:
                return False
            if pre[i]==[]:
                return True
            visited.add(i)
            for crs in pre[i]:
                if not dfs(crs,visited):
                    return False
            visited.remove(i)
            pre[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i,set()):
                return False
        return True



            



