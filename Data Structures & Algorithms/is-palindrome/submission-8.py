class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        l,r = 0,len(s)-1
        print(s)
        while l<r:
            if s[l]!=s[r]:
                print(l)
                print(r)
                return False
            l+=1
            r-=1
            
        return True