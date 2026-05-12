class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int l = 0;
        int r = people.size()-1;
        int max = 0;
        while(l<=r){
            int num = limit - people[r--];
            max++;
            if(l<=r && num>=people[l]){
                l++;
            }
        }
        return max;
    }
};