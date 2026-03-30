class StockSpanner:

    def __init__(self):
        self.stack = [] # contains (stock, span)
        
    def next(self, price: int) -> int:
        span = 1
        stack = self.stack
        while stack and stack[-1][0] <= price:
            prev = stack.pop()
            span += prev[1]
        stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)