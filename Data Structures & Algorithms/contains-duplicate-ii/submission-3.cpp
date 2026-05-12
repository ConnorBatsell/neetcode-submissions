class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> mySet;
        int l=0;
        for(int r=0; r<nums.size(); r++){
            if(r-l>k){
                mySet.erase(nums[l]);
                l++;
            }
            if(mySet.find(nums[r])!=mySet.end()){
                return true;
            }
            mySet.insert(nums[r]);
        }
        return false;
    }
};