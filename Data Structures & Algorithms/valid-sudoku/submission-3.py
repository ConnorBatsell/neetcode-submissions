class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                a = board[r][c]
                if a==".":
                    continue
                elif a in rows[r] or a in cols[c] or a in squares[(r//3, c//3)]:
                    return False
                rows[r].add(a) 
                cols[c].add(a)
                squares[(r//3, c//3)].add(a)
        return True

