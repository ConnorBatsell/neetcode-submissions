class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        for(int i=0; i<nums.size(); i++){
            for(int j=0; j<nums.size(); j++){
                if(i!=j){
                    if(nums[i]==nums[j]){
                        nums[j] = INT_MIN;
                    }
                }
            }
        }
        nums.erase(remove(nums.begin(), nums.end(), INT_MIN),nums.end());
        return nums.size();
    }
};