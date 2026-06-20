class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        a = []
        def dfs(start):
            if start == len(s):
                res.append(a.copy())
                return
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if piece == piece[::-1]:   # piece is a palindrome
                    a.append(piece)
                    dfs(end)
                    a.pop()
        dfs(0)
        return res

