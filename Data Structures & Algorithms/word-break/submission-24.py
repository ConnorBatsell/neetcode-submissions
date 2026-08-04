class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        dp = [None]*len(s)
        def dfs(i):
            if i>=len(s):
                return True
            if dp[i] is not None:
                return dp[i]
            for word in wordDict:
                if i+len(word)<=len(s) and s[i:i+len(word)]==word:
                    dp[i] = dfs(i+len(word)) 
                    if dp[i]:
                        return True
            dp[i] = False
            return dp[i]
            
        return dfs(0)



                

        
