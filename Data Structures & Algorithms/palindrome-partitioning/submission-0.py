class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        a = []
        def dfs(start, path):
            if start == len(s):
                res.append(path.copy())
                return
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if piece == piece[::-1]:   # piece is a palindrome
                    path.append(piece)
                    dfs(end, path)
                    path.pop()
        dfs(0, a)
        return res

