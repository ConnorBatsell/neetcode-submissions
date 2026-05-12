class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequencies;
        for(int i=0; i<nums.size(); i++){
            frequencies[nums[i]]++;
        }
        priority_queue<pair<int,int>> pq;
        for(auto& p: frequencies){
            pq.push({p.second, p.first});
        }
        vector<int> result;
        for(int i=0; i<k; i++){
            result.push_back(pq.top().second);
            pq.pop();
        }
        return result;
    }
};
