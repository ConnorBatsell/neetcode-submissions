class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        prof = 0
        for price in prices:
            if price < l:
                l = price
            elif price-l>prof:
                prof = price-l
        return prof 