class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        res,l = 0,0
        for r,c in enumerate(s):
            if c in cache:
                l = max(l,cache[c]+1)
            cache[c] = r
            res = max(res, r-l+1)
        return res

        