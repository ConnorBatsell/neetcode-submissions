class Solution {
public:

    string encode(vector<string>& strs) {
        string final;
        for(string st : strs){
            final += to_string(st.size()) + "#" + st;
        }
        cout << final;
        return final;
    }

    vector<string> decode(string s) {
        string temp;
        vector<string> strs;
        string tempWord;
        int n=0;
        for(int i=0; i<s.size(); i++){
            if(n>0){
                tempWord +=s[i];
                n--;
                if(n==0){
                    strs.push_back(tempWord);
                }
            }
            else if(s[i]=='#'){
                n = stoi(temp);
                temp.clear();
                tempWord.clear();
                if (n == 0) {              
                    strs.push_back("");
                }
            }
            else{
                temp += s[i];
            }
        }
        return strs;
    }
};
