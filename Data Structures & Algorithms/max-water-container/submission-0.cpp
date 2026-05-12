class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size()-1;
        int maxW = 0;
        while(l<r){
            int water = (r-l) * min(heights[l], heights[r]);
            maxW = max(water, maxW);
            if(heights[l]<=heights[r]){
                l++;
            }
            else if(heights[r]<=heights[l]){
                r--;
            }
        }
        return maxW;
    }
};
