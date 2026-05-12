class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        unordered_map<int, int> freq;
        for(int i=0; i<nums.size(); i++){
            freq[nums[i]]++;
        }
        int counter;
        for(int i=0; i<nums.size(); i++){
            if(freq.find(i+1) == freq.end()){
                return i+1;
            }
            counter = i+1;
        }
        return counter+1;
    

    }
};