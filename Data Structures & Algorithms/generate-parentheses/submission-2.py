class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []
        def dfs(o,c):
            if o==n and c==n:
                res.append("".join(s.copy()))
                return
            if o<n:
                s.append("(")
                dfs(o+1, c)
                s.pop()
            if c<o:
                s.append(")")
                dfs(o,c+1)
                s.pop()
        dfs(0,0)
        return res