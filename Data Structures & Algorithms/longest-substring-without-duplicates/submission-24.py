class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        l,r = 0,0
        maxLen = 0
        while r<len(s):
            if s[r] in cache:
                l = max(l,cache[s[r]]+1)
            cache[s[r]] = r
            maxLen = max(maxLen, r-l+1)
            r+=1
        return maxLen

        