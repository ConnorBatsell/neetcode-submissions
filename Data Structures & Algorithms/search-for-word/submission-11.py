class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r,c, idx):
            if idx==len(word):
                return True
            if min(r,c)<0 or r==rows or c==cols or (r,c) in visited or board[r][c]!=word[idx]:
                return False
            idx+=1
            visited.add((r,c))
            found =  dfs(r+1,c,idx) or dfs(r-1,c,idx) or dfs(r,c+1,idx) or dfs(r,c-1,idx)
            visited.remove((r,c))
            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
            