class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int l=0;
        vector<int> res;
        for(int r=k-1; r<nums.size(); r++){
            int a = l;
            int m=INT_MIN;
            while(a<=r){
                m = max(m, nums[a]);
                a++;
            }
            res.push_back(m);
            l++;
        }
        return res;
    }
};
