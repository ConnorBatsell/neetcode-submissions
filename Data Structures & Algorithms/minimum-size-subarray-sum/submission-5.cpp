class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l=0;
        int sum=0;
        int minLen = 0;
        bool exist = false;
        for(int r=0; r<nums.size(); r++){
            sum += nums[r];
            while(sum>=target){
                if(!exist){
                    minLen = nums.size();
                }
                exist = true;
                if(r-l+1 < minLen){
                    minLen = r-l+1;
                }
                sum-=nums[l];
                l++;
            }
        }
        return minLen;
    }
};