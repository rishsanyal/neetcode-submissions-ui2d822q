"""
we have to maintain a queue with a limited capcity

We maintain a head and a tail -> Could also add all the way in the end

We track the total number of elements in the node too 
"""

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.k = k
        self.ctr = 0

    def enQueue(self, value: int) -> bool:
        if self.ctr == self.k:
            return False

        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

        self.tail.next = self.head
        self.ctr += 1

        return True
        

    def deQueue(self) -> bool:
        if self.ctr == 0:
            return False
        
        self.ctr -= 1

        if self.isEmpty():
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        return True
        

    def Front(self) -> int:
        return self.head.val if self.head else -1

    def Rear(self) -> int:
        temp = self.head
        temp_c = self.ctr

        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return self.ctr == 0

    def isFull(self) -> bool:
        return self.ctr == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()