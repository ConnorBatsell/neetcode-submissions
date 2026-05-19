class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow=0;
        int fast=0;
        while(true){
            slow = nums[slow];
            fast = nums[nums[fast]];
            if(slow==fast){
                break;
            }
        }
        int curr=0;
        while(curr!=slow){
            curr = nums[curr];
            slow = nums[slow];
        }
        return slow;
    }
};
