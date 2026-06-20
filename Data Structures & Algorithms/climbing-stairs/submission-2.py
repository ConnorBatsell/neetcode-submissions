class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = {}
        def helper(curr):
            if curr in self.dp:
                return self.dp[curr]
            if curr<=0:
                if curr==0:
                    return 1
                return 0
            self.dp[curr] = helper(curr-2) + helper(curr-1)
            return self.dp[curr]
        return helper(n)
        