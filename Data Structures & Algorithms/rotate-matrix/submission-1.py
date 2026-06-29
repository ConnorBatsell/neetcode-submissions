class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)//2):
            temp = matrix[i]
            matrix[i] = matrix[len(matrix)-i-1]
            matrix[len(matrix)-i-1] = temp
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        