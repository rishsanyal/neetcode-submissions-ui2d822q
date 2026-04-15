"""
Similar to the last question:

on next -> 
calculate span
    - check the top element and if it's value is lte then get it's span + 1
    - else return 1
push on stack with the stock's span
but then why do we need a stack? Don't we just need the last number?

We could optimize with a monotonic stack?

["StockSpanner","next","next","next","next","next","next","next"]
[[],[100],[80],[60],[70],[60],[75],[85]]

70,
80, 1
100, 1
"""

class StockSpanner:

    def __init__(self):
        # (stock price, span)
        self.stack = []
        
    def next(self, price: int) -> int:
        result = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            result += prev_span

        self.stack.append((price, result))

        return result


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)