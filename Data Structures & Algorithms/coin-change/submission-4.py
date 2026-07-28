class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(amt):
            if amt==0:
                return 0
            if amt in cache:
                return cache[amt]

            res = 1e9
            for coin in coins:
                
                temp=amt-coin
                if temp>=0: 
                    res = min(res, 1+dfs(temp))
            cache[amt] = res
            return res
        minCoins = dfs(amount)
        return -1 if minCoins >=1e9 else minCoins
            