class Solution {
public:
    int characterReplacement(string s, int k) {
        int l=0;
        unordered_map<char, int> temp;
        int f=0;
        int maxN=0;
        for(int r=0; r<s.size(); r++){
            temp[s[r]]++;
            f = max(f, temp[s[r]]);
            if((r-l+1)-f>k){
                temp[s[l]]--;
                l++;
            }
            maxN = max(r-l+1, maxN);
        }
        return maxN;
    }
};
