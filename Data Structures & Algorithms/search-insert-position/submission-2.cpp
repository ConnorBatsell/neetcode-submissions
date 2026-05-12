class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return bsearch(0, nums.size(), nums, target);
    }
    int bsearch(int l, int r, vector<int>& nums, int target){
        if(l>r){
            if(l>nums.size()){
                return l-1;
            }
            return l;
        }
        int m = l + (r-l) / 2;
        if(nums[m]==target){
            return m;
        }
        if(nums[m]>target){
            return bsearch(l,m-1, nums, target);
        }
        else{
            return bsearch(m+1, r, nums, target);
        }
        
    }
};