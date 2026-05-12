class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> record;

        for(string op : operations){
            if(op == string(1,'+')){
                record.push_back(record[record.size()-1] + record[record.size()-2]);
            }
            else if(op==string(1,'D')){
                record.push_back(2*record[record.size()-1]);
            }
            else if(op==string(1,'C')){
                record.pop_back();
            }
            else{
                record.push_back(stoi(op));
            }
        }
        int sum=0;
        for(int x: record){
            sum += x;
        
        }
        return sum;
    }
};