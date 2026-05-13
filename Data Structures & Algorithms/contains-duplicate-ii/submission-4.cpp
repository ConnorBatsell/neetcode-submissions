class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> temp;
        int i=0;
        for(int j=0; j<nums.size(); j++){
           if(j-i>k){
                temp.erase(nums[i]);
                i++;
           }
           if(temp.contains(nums[j])){
                return true;
           }
           temp.insert(nums[j]);
        }
        return false;
    }
};