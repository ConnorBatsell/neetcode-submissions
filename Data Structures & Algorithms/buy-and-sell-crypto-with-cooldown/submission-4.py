class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)
        def recurse(i, bought):
            if i>=len(prices):
                return 0
            if (i,bought) in dp:
                return dp[(i,bought)]
            if bought:
                res = max(prices[i] + recurse(i+2, False), recurse(i+1, True))
            else:
                res = max(-prices[i] + recurse(i+1, True), recurse(i+1, False))
            dp[(i,bought)] = res
            return dp[(i,bought)]
        return recurse(0,False)