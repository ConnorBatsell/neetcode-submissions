class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLen = 0;
        unordered_set<char> temp;
        int l = 0;
        for(int r=0; r<s.size(); r++){
            while(temp.contains(s[r])){
                temp.erase(s[l]);
                l++;
            }
            temp.insert(s[r]);
            if(temp.size() > maxLen){
                maxLen = temp.size();
            }
        }
        return maxLen;


    }
};
