class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxk = 1;
        int l=1;
        for(int i=0; i<piles.size(); i++){
            if(piles[i]>maxk){
                maxk = piles[i];
            }
        }
        int r = maxk;
        int res = maxk;
        while(l<=r){
            int m = l+(r-l)/2;
            long long time = 0;
            for(int pile: piles){
                time += (pile + m-1)/m;
            }
            if(time <= h){
                res = m;
                r = m-1;
            }
            else{
                l = m+1;
            }
        }
        return res;
    }
    
};
