class StockSpanner:

    def __init__(self):
        self.s = [] #price, span

    def next(self, price: int) -> int:
        span = 1
        while self.s and self.s[-1][0]<= price:
            stackPrice, stackSpan = self.s.pop()
            span += stackSpan
        self.s.append([price,span])
        return span
            




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)