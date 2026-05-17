class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int, int> a;
        for(int i=0; i<nums.size(); i++){
            a[nums[i]]++;
            if(a[nums[i]]>1){
                return nums[i];
            }
        }
        return 0;
    }
};
