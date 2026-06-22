class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = defaultdict(int)

        def dfs(i):
            if i>=len(s):
                dp[i] = True
                return dp[i]
            if i in dp:
                return dp[i]
            res = False
            for word in wordDict:
                if s[i:i+len(word)]==word:
                    if dfs(i+len(word)):
                        res = True
                        break
            dp[i] = res
            return res
        return dfs(0)
