class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        for a,b in prerequisites:
            pre[a].append(b)
        out = []
        visit = set()
        ans = set()
        def dfs(i):
            if i in visit:
                return False
            if i in ans:
                return True
            visit.add(i)
            for j in pre[i]:
                if not dfs(j):
                    return False
            visit.discard(i)
            ans.add(i)
            out.append(i)
            return True
        for j in range(numCourses):
            if not dfs(j):
                return []
        return out