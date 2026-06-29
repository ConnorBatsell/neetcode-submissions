class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols = [False for i in range(len(matrix[0]))]
        rows = [False for i in range(len(matrix))]
        print(cols)
        print(rows)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    cols[j] = True
                    rows[i] = True
        for i in range(len(rows)):
            for j in range(len(cols)):
                if cols[j] or rows[i]:
                    matrix[i][j] = 0
        

    
         