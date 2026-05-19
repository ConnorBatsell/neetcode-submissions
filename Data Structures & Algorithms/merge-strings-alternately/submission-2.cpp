class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string output;
        int l=0;
        int r=0;
        while(l<word1.size() || r<word2.size()){
            if(l<word1.size()){
                output+=word1[l++];
            }
            if(r<word2.size()){
                output+=word2[r++];
            }
        }
        return output;
    }
};