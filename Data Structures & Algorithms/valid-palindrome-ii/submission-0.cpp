class Solution {
public:
    bool validPalindrome(string s) {
        string temp = s;
        for(int i=0; i<s.size(); i++){
            cout << i;
            temp.erase(i, 1);
            int l=0;
            int r = temp.size()-1;
            bool valid = true;
            while(l<r){
                while(l<r && !alphaNum(temp[l])){
                    l++;
                }
                while(r>l && !alphaNum(temp[r])){
                    r--;
                }
                if(temp[r]!=temp[l]){
                    valid = false;
                }
                l++;
                r--;
            }
            if(valid){
                return true;
            }
            temp = s;
        }
        return false;
    }
    bool alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
};