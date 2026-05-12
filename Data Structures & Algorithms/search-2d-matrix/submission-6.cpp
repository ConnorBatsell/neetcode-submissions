class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l=0;
        int r=matrix.size()-1;
        while(l<r){
            int m = l+(r-l)/2;
            if(target > matrix[m][matrix[0].size()-1]){
                l=m+1;
            }
            else if(target < matrix[m][0]){
                r=m-1;
            }
            else{
                break;
            }
        }
        int l2 =0;
        int row = (l+r)/2;
        int r2 = matrix[row].size();
        while(l2<=r2){
            int m = l2+(r2-l2)/2;
            if(matrix[row][m] < target){
                l2 = m+1;
            }
            else if(matrix[row][m] > target){
                r2 = m-1;
            }
            else{
                return true;
            }
        }
        return false;

    }
};
