class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> pq;
        vector<int> ms;
        for(int r=0; r<nums.size(); r++){
            pq.push({nums[r],r});
            if(r>=k-1){
                while(pq.top().second<=r-k){
                    pq.pop();
                }
                ms.push_back(pq.top().first);
            }
            
        }
        return ms;
    }
};
