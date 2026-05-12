class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> numArr(3);
        for(int i=0; i<nums.size(); i++){
            numArr[nums[i]]++;
        }
        int count = 0;
        for(int i=0; i<3; i++){
            for(int j=0; j<numArr[i]; j++){
                nums[count] = i;
                count++;
            }
        }
    }
};