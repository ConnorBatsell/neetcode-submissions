class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> temp;
        int l=0;
        int maxSize = 0;
        for(int r=0; r<s.size(); r++){
            if(temp.contains(s[r])){
                l = max(temp[s[r]]+1, l);
                temp.erase(s[r]);
            }
            temp[s[r]]=r;
            maxSize = max(maxSize, r-l+1);
        }
        return maxSize;
    }
};
