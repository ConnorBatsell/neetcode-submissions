class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> set1;
        unordered_map<char, int> set2;
        int l=0;
        for(int i=0; i<s1.size(); i++){
            set1[s1[i]]++;
        }
        for(int r=0; r<s2.size(); r++){
            set2[s2[r]]++;
            if(r-l+1>s1.size()){
                set2[s2[l]]--;
                if(set2[s2[l]]==0){
                    set2.erase(s2[l]);
                }
                l++;
            }
            if(set1==set2){
                return true;
            }
        }
        return false;
    }
};
