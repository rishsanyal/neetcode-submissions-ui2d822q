"""
Using a heap makes everything O(nlgn) -> because of heap insertion which is log(n)

We could use a tracker number but updating that will be a hassle, right?

OHHH we track the min number at EVERY POINT in the stack

We insert the value AND the min number at that point, in the stack
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = None

    def push(self, val: int) -> None:

        if not self.min_num or self.min_num > val:
            self.min_num = val

        self.stack.append((val, self.min_num))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
