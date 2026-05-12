#include <string>

class Solution {
public:
    int calPoints(vector<string>& operations) {
        int score = 0;
        stack<int> s;
        for(int i=0; i<operations.size(); i++){
            
            if(operations[i]=="D"){
                s.push(s.top()*2);
            }
            else if(operations[i]=="+"){
                int first = s.top(); 
                s.pop();

                int temp = s.top() + first;
                s.push(first);
                s.push(temp);
            }
            else if(operations[i]=="C"){
                s.pop();
            }
            else{
                s.push(stoi(operations[i]));
            }
        }
        while (!s.empty()) {
            score += s.top();
            s.pop();
        }
        return score;
    }
};