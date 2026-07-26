class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        def dfs(i):
            if i>=len(s):
                res.append(subset.copy())
                return
            for j in range(i,len(s)):
                if self.pali(i,j,s):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
        dfs(0)
        return res

    def pali(self, l,r,s):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True




