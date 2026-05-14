class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l=0;
        int sum =0;
        int size=INT_MAX;
        for(int r=0; r<nums.size(); r++){
            sum+=nums[r];
            while(sum>=target){
                size = min(r-l+1, size);
                sum-=nums[l];
                l++;
                
            }
        }
        return size==INT_MAX ? 0:size;
    }
};