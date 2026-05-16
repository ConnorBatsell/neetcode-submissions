class Solution {
public:
    string minWindow(string s, string t) {
        if(t.empty()){
            return "";
        }
        unordered_map<char, int> temp;
        for(int i=0; i<t.size(); i++){
            temp[t[i]]++;
        }
        int l=0;
        unordered_map<char, int> temp2;
        int have=0;
        int need = temp.size();
        int shortest=INT_MAX;
        vector<int> pear(2);
        for(int r=0; r<s.size(); r++){
            temp2[s[r]]++;
            if(temp.contains(s[r]) && temp2[s[r]]==temp[s[r]]){
                have++;
            }
            while(have==need){
                if(r-l+1 < shortest){
                    shortest = r-l+1;
                    pear[0] = l;
                    pear[1] = r;
                }
                temp2[s[l]]--;
                if(temp.contains(s[l]) && temp2[s[l]]<temp[s[l]]){
                    have--;
                }
                l++;
            }
        }
        return shortest == INT_MAX ? "" : s.substr(pear[0], pear[1]-pear[0]+1);


    }
};
