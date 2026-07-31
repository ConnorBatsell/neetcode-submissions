class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [-1]*len(s)
        def dfs(i):
            if i>=len(s):
                return 1
            if s[i]=='0':
                return 0
            if cache[i]!=-1:
                return cache[i]
            out = 0
            if len(s[i:])>=2:
                if int(s[i:i+2])<=26:
                    out+= dfs(i+2)
            out += dfs(i+1)
            cache[i] = out
            return cache[i]
        return dfs(0)
