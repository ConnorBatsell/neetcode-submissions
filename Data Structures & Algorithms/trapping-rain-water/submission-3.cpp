class Solution {
public:
    int trap(vector<int>& height) {
        int total =0;
        for(int i=0; i<height.size(); i++){
            int l= i;
            int leftMax =i;
            int r= i;
            int rightMax = i;
            while(l>0){
                l--;
                if(height[l]>height[leftMax]){
                    leftMax = l;
                }
            }
            while(r < height.size()-1){
                r++;
                if(height[r]>height[rightMax]){
                    rightMax = r;
                }
            }
            total += max(min(height[leftMax], height[rightMax]) - height[i], 0);

        }
        return total;
    }
};
