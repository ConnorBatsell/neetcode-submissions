class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> sortMap;
        for(int i=0; i<strs.size(); i++){
            string sorted = strs[i];
            sort(sorted.begin(), sorted.end());
            sortMap[sorted].push_back(strs[i]);
        }
        vector<vector<string>> result;
        for(const auto& p : sortMap){
            result.push_back(p.second);
        }
        return result;
    }
};
