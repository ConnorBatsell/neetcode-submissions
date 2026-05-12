class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l=0;
        int r=1;
        int maxP = 0;
        while(r<prices.size()){
            if(prices[r] > prices[l]){
                maxP = max(prices[r]-prices[l], maxP);
            }
            if(prices[r] < prices[l]){
                l = r;
            }
            r++;
        }
        return maxP;
    }
};
