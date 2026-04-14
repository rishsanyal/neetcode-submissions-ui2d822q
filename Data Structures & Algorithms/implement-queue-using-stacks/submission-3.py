class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop(-1)

    def __bool__(self):
        return bool(self.stack)

    def __repr__(self):
        return str(self.stack)


class MyQueue:

    def __init__(self):
        self.s1, self.s2 = Stack(), Stack()

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.push(self.s1.pop())
        self.s2.push(x)

        while self.s2:
            self.s1.push(self.s2.pop())

        print(self.s1)

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1.stack[-1]

    def empty(self) -> bool:
        return bool(self.s1.stack == [])


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()