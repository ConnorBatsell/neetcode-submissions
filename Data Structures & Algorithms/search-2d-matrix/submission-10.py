class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        print(r)
        row = 0
        while(l<=r):
            m = l + ((r-l)//2)
            if matrix[m][0] > target:
                r = m-1
            elif matrix[m][0] < target:
                row= m
                l = m+1
            else:
                return True
        print(row)
        l2=0
        r2=len(matrix[row])-1
        while(l2<=r2):
            m = l2 + ((r2-l2)//2)
            if matrix[row][m]>target:
                r2 = m-1
            elif matrix[row][m] < target:
                l2 = m+1
            else:
                return True
        return False

        