class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProf =0;
        for(int i=0; i<prices.size(); i++){
            for(int j=i+1; j<prices.size(); j++){
                int tempProf = prices[j] - prices[i];
                if(tempProf>maxProf){
                    maxProf = tempProf;
                }
            }
        }
        return maxProf;
    }
};
