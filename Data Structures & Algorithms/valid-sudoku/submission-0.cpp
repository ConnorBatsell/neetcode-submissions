class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i=0; i<board.size(); i++){
            unordered_map<char, int> vals;
            for(int j=0; j<board[0].size(); j++){
                char ch = board[i][j];
                if(ch == '.'){
                    continue;
                }
                vals[ch]++;
            }
            for(auto& p: vals){
                if(p.second>1){
                    return false;
                }
            }
        }
        for(int i=0; i<board[0].size(); i++){
            unordered_map<char, int> vals;
            for(int j=0; j<board.size(); j++){
                char ch = board[j][i];
                if(ch == '.'){
                    continue;
                }
                vals[ch]++;
            }
            for(auto& p: vals){
                if(p.second>1){
                    return false;
                }
            }
        }
        for (int b = 0; b < 9; b++) {
            int sr = (b / 3) * 3;
            int sc = (b % 3) * 3;
            unordered_map<char, int> vals;

            for (int r = sr; r < sr + 3; r++) {
                for (int c = sc; c < sc + 3; c++) {
                    char ch = board[r][c];
                    if (ch == '.') continue;
                    if (++vals[ch] > 1) return false;
                }
            }
        }
        return true;
    }
};
