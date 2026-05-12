class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        unordered_map<char, char> matches = {{')', '('}, {']', '['}, {'}', '{'}};
        for(char c: s){
            if(matches.count(c)){
                if(!stack.empty() && stack.top()==matches[c]){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stack.push(c);
            }
        }
        if(stack.empty()){
            return true;
        }
        return false;
    }
};
