class Solution {
public:
    bool isPalindrome(string s) {
        s.erase(remove(s.begin(), s.end(), ' '), s.end());
        s.erase(remove_if(s.begin(), s.end(),[](unsigned char c) {return !isalnum(c);}),s.end());
        transform(s.begin(), s.end(), s.begin(),[](unsigned char c) {return std::tolower(c);});
        cout << s;
        
        int start = 0;
        int end = s.size()-1;
        while(start<end){
            if(s[start]!=s[end]){
                cout << "error"; 
                cout << s[start] << ".";
                cout << s[end] << ".";
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};
