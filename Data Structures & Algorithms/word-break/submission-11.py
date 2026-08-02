class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        temp = ""
        extra = ""
        for i in range(len(s)):
            temp+=s[i]
            extra += s[i]            
            if temp in wordDict:
                temp = ""
            elif extra in wordDict:
                extra = ""
                
        if not temp=="" and not extra=="":
            return False
        return True


                

        
