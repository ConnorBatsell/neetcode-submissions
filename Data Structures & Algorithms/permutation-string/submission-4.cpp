class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> map1;
        unordered_map<char, int> map2;
        for(int i=0; i<s1.size(); i++){
            map1[s1[i]]++;
        }
        int l=0;
        for(int r=0; r<s2.size(); r++){
            map2[s2[r]]++;
            while(map2.size()>map1.size() || map2[s2[r]] > map1[s2[r]]){
                map2[s2[l]]--;
                if(map2[s2[l]]==0){
                    map2.erase(s2[l]);
                }
                l++;
            }
            if(map1==map2){
                return true;
            }
        }
        return false;
    }
};
