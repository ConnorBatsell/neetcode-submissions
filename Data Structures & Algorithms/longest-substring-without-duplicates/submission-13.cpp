class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> temp;
        int l=0;
        int maxSize = 0;
        for(int r=0; r<s.size(); r++){
            while(temp[s[r]]>0){
                temp[s[l]]--;
                if(temp[s[l]]==0){
                    temp.erase(s[l]);    
                }
                l++;
            }
            temp[s[r]]++;
            maxSize = max((int)temp.size(), maxSize);
        }
        return maxSize;
    }
};
