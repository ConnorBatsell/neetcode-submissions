class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        prof = 0
        for price in prices:
            prof = max(prof, price-minBuy)
            minBuy = min(minBuy, price)
        return prof 