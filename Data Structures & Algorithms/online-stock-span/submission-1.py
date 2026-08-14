"""

(price, span) in a stack

While forming the stack, we see if the previous number is lte the current number
If so, we add one to it's stack

else we make the span 0 and go from there

on every next
- we pop until we run out of stock or hit a value gt the current number
- we add the span to the stock and provide the answer


[
    (100, 1)
    (85, 6)
]

"""


class StockSpanner:
    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        curr_span = 1

        if not self.stack or self.stack[-1][0] > price:
            self.stack.append(
                (price, curr_span)
            )
            return curr_span

        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            curr_span += prev_span

        self.stack.append((price, curr_span))

        return curr_span

            



        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)