class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix;
        for(int j=0; j<strs[0].length(); j++){
            char a = strs[0][j];
            for(string str : strs){
                if(str[j]!=a){
                    return prefix;
                }
            }
            prefix= prefix + a;
        }
        return prefix;    
    }
};