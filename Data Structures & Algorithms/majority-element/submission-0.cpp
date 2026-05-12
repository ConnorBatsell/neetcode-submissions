class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(int i=0; i<nums.size(); i++){
            mp[nums[i]]++;
        }
        int max = 0;
        int maxKey = 0;

        for (const auto& p : mp) {
            if(p.second > max){
                max = p.second;
                maxKey = p.first; 
            }
        }
        return maxKey;
    }
};