class Solution {
public:
    string minWindow(string s, string t) {
        if(t.empty()){
            return "";
        }
        unordered_map<char, int> countT;
        for(int i=0; i<t.size(); i++){
            countT[t[i]]++;
        }
        unordered_map<char, int> window;
        int have=0;
        int need = countT.size();
        pair<int,int> res = {-1,-1};
        int resLen = INT_MAX;
        int l=0;
        for(int r=0; r<s.size(); r++){
            window[s[r]]++;
            if(countT.contains(s[r]) && window[s[r]]==countT[s[r]]){
                have++;
            }
            while(have==need){
                if(r-l+1 < resLen){
                    resLen = r-l+1;
                    res = {l,r};
                }
                window[s[l]]--;
                if(countT.contains(s[l]) && window[s[l]]<countT[s[l]]){
                    have--;
                }
                l++;
            }
        }
        return resLen == INT_MAX ? "" : s.substr(res.first, resLen);
    }
};
