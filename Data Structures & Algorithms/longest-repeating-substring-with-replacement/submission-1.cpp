class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> temp;
        int l=0, f=0;
        int maxLen=0;
        for(int r=0; r<s.size(); r++){
            temp[s[r]]++;
            f = max(f, temp[s[r]]);
            while((r-l+1)-f>k){
                temp[s[l]]--;
                l++;
            }
            maxLen = max(maxLen, r-l+1);
        }
        return maxLen;
    }
};
