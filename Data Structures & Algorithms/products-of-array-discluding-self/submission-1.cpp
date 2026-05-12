class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> output;
        vector<int> prefix;
        vector<int> suffix(nums.size());
        int preProduct = 1;
        int sufProduct = 1;
        prefix.push_back(preProduct);
        suffix[nums.size()-1] = (sufProduct);
        for(int i=1; i<nums.size(); i++){
            preProduct *= nums[i-1];
            prefix.push_back(preProduct);
        }
        for(int i=nums.size()-2; i>=0; i--){
            sufProduct*= nums[i+1];
            suffix[i] = (sufProduct);
        }
        for(int i=0; i<nums.size(); i++){
            output.push_back(prefix[i]*suffix[i]);
        }
        return output;
        
    }
};
