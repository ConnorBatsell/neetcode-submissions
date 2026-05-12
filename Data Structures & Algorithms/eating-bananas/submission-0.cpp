class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxk = 1;
        for(int i=0; i<piles.size(); i++){
            if(piles[i]>maxk){
                maxk = piles[i];
            }
        }
        for(int i=1; i<=maxk; i++){
            long long totalT = 0;
            for(int pile : piles){
                totalT += (pile + i-1)/i;
            }
            if(totalT <= h){
                return i;
            }
        }
    }
    
};
