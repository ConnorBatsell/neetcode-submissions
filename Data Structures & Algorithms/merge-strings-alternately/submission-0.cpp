class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string final;
        int firstIndex = 0;
        int secondIndex = 0;
        for(int i=0; i<(word1.size() + word2.size()); i++){
            if(firstIndex != word1.size()){
                final += word1[firstIndex];
                firstIndex++;
            }
            if(secondIndex != word2.size()){
                final += word2[secondIndex];
                secondIndex++;
            }
        }
        return final;
    }
};