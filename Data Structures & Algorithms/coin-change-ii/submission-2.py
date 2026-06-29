class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = defaultdict(int)
        def helper(i, amt):
            if amt==amount:
                return 1
            if amt>amount:
                return 0
            count = 0
            if (i,amt) in cache:
                return cache[(i,amt)]    
            for j in range(len(coins)-i):
                    count += helper(i+j, amt+coins[i+j])
            cache[(i, amt)] = count
            return count
        return helper(0,0)
