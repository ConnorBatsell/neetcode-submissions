class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        prices = [INF]*n
        prices[src] = 0
        for i in range(k+1):
            tmp = prices.copy()
            for src,dest,price in flights:
                if prices[src]==INF:
                    continue
                if prices[src]+price < tmp[dest]:
                    tmp[dest] = prices[src]+price
            prices = tmp
        return -1 if prices[dst]==INF else prices[dst]
                

            