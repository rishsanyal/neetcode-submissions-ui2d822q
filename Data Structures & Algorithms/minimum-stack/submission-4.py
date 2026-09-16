class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = None

    def push(self, val: int) -> None:
        if not self.curr_min:
            self.curr_min = val

        self.curr_min = min(self.curr_min, val)
        self.stack.append((val, self.curr_min))
        
    def pop(self) -> None:
        _, prev_min = self.stack.pop()

        if self.stack:
            self.curr_min = self.stack[-1][1]
        else:
            self.curr_min = None
        
    def top(self) -> int:
        if not self.stack:
            return -1

        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.curr_min
        
