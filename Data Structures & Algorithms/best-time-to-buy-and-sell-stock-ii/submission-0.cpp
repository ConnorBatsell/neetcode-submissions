class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        for(int i=0; i<prices.size(); i++){
            int currNum = prices[i];
            if(i!=prices.size()-1){
                int dayDiff = prices[i+1]-currNum;
                if(dayDiff>0){
                    max += dayDiff;
                }
            }
        }
        return max; 
    }
};