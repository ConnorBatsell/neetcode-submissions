#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> lenMap;

        for (int i = 0; i < nums.size(); i+=1) {
            lenMap[nums[i]] = 0;
        }

        if (lenMap.size() != nums.size()) {
            return true;
        } else {
            return false;
        }

        
    }
};