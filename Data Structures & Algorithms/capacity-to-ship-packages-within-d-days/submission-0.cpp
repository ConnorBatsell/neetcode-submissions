class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int l = *max_element(weights.begin(), weights.end());
        int r = accumulate(weights.begin(), weights.end(), 0);
        int res = r;
        while(l<=r){
            int cap = l + (r-l)/2;
            if(testcap(weights, days, cap)){
                if(cap<res){
                    res = cap;
                }
                r = cap-1;
            }
            else{
                l = cap+1;
            }
        }
        return res;

    }
    bool testcap(vector<int>& weights, int days, int cap){
        int ships = 1;
        int currcap = cap;
        for(int w: weights){
            if(currcap-w < 0){
                ships+=1;
                currcap = cap;
            }
            currcap -= w;
        }
        return ships <= days;
    }
};