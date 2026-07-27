class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 
        for l in range(len(s)):
            for r in range(l, len(s)):
                if self.palindrome(s[l:r+1]):
                    res+=1
        return res

    def palindrome(self, s):
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True