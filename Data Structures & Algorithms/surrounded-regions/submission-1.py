class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, visited):
            if (min(r,c)<0 or r==rows or c==cols or (r,c) in visited or board[r][c]=='X'):
                return
            board[r][c]="#"
            visited.add((r,c))
            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)

        for r in range(rows):
            dfs(r,0,set())
            dfs(r,cols-1,set())
        for c in range(cols):
            dfs(0,c,set())
            dfs(rows-1,c,set())
            print(board)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="#":
                    board[r][c]="O"
                
            
        
        

