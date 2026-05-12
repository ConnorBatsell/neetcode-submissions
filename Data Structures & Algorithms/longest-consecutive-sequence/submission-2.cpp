class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        unordered_map<int, int> freqCount;
        int lastKey;
        if(nums.size()==0){
            return 0;
        }
        for(int i=0; i<nums.size(); i++){
            int num = nums[i];
            if(numSet.count(num-1)==0){
                freqCount[num] = 1;
            }
        }
        for(auto& [key, val] : freqCount){
            int currNum = key+1;
            while(numSet.count(currNum)>0){
                freqCount[key]++;
                currNum++;
            }
        }
        int maxVal = INT_MIN;
        int maxKey;
        for (const auto& [key, val] : freqCount) {
            if (val > maxVal) {
                maxVal = val;
                maxKey = key;
            }
        }
        return maxVal;
    }
};
