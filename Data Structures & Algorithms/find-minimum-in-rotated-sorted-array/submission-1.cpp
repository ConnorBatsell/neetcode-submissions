class Solution {
public:
    int findMin(vector<int> &nums) {
        int l=0;
        int r = nums.size()-1;
        int minV = nums[0];
        while(l<=r){
            int m = l + (r-l)/2;
            if(nums[l] < nums[r]){
                minV = min(minV,nums[l]);
                break;
            }
            minV = min(minV,nums[m]);
            if(nums[m]>=nums[l]){
                l = m+1;
            }
            else{
                r = m-1;
            }
        }
        return minV;
    }
};
