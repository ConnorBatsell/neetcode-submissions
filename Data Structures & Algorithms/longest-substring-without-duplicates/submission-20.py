class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = {}
        l=0
        out =0
        for r in range(len(s)):
            if s[r] in temp:
                l = max(temp[s[r]]+1, l)
            temp[s[r]] = r
            out = max(out, r-l+1)
        return out

        