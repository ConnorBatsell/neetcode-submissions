class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        for a,b in prerequisites:
            pre[a].append(b)
        visited = set()
        out = []
        ans = set()
        def dfs(i):
            if i in visited:
                return False
            if i in ans:
                return True
            visited.add(i)
            for crs in pre[i]:
                if not dfs(crs):
                    return False
            visited.remove(i)
            ans.add(i)
            out.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return out