class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int, int> freq;
        vector<int> final;
        for(int i=0; i<nums.size(); i++){
            freq[nums[i]]++;
        }
        for(auto& [key, val]: freq){
            if(val > floor(nums.size()/3)){
                final.push_back(key);
            }
        }
        return final;
    }
};