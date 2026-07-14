class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        l = 0
        maxLen = 0
        for r,c in enumerate(s):
            if c in cache:
                l = max(l,cache[c]+1)
            cache[c] = r
            maxLen = max(maxLen, r-l+1)
        return maxLen

        