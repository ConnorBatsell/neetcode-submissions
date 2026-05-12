class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLen = 0;
        unordered_map<char, int> temp;
        int l = 0;
        for(int r=0; r<s.size(); r++){
            if(temp.contains(s[r])){
                l = max(temp[s[r]]+1, l);
                temp.erase(s[r]);
            }
            temp[s[r]] = r;
            if((r-l+1)>maxLen){
                maxLen = r-l+1;
            }
        }
        return maxLen;


    }
};
