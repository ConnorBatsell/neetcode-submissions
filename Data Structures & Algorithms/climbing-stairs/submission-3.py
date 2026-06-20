class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def helper(curr):
            if curr in dp:
                return dp[curr]
            if curr<=0:
                if curr==0:
                    return 1
                return 0
            dp[curr] = helper(curr-2) + helper(curr-1)
            return dp[curr]
        return helper(n)
        