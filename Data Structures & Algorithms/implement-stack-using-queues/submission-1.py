"""
Stack - LIFO

Queue - FIFO
Insert in the end but pop from the front

stack -> add to the queue, 
"""

class Queue:
    def __init__(self):
        self.q = []

    def push(self, val):
        self.q.append(val)

    def pop(self):
        if self.q:
            return self.q.pop(0)
        return None

    def __bool__(self):
        return bool(len(self.q))

    def __repr__(self):
        print(self.q)
        return ''


class MyStack:

    def __init__(self):
        self.q_1 = Queue()
        self.q_2 = Queue()

    def push(self, x: int) -> None:
        self.q_2.push(x)

        while self.q_1:
            self.q_2.push(self.q_1.pop())

        self.q_2, self.q_1 = self.q_1, self.q_2

    def pop(self) -> int:
        # print(self.q_1, self.q_2)
        return self.q_1.pop()

    def top(self) -> int:
        return self.q_1.q[0] or -1
        
    def empty(self) -> bool:
        return not bool(self.q_1)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()