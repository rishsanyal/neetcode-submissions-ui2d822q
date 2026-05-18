
"""
We can make our own nodes
- Doubly linkedList
- Hash for values


On every get or put, we need to take the node out and put it in the front of the linkedlist
- How do we avoid getting O(N) time for the last node?
- We track the tail value in the class - Everytime we remove the tail, we replace it with the previous Node



["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]

- {1: 1}
- {2:2, 1:1}
- {1:1, 2:2}
- {1:1, 3:3}


"""

class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = self.head
        self.capacity = capacity

        # key, node
        self.tracker = {}

    def __delete_node(self):
        if self.tail:
            key = self.tail.key

            print("Tail key ->", key)

            self.tracker.pop(key)

            self.tail = self.tail.prev

            if self.tail:
                self.tail.next = None

    def __update_node(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        elif node == self.head == self.tail:
            return
        elif node == self.tail:
            self.tail = self.tail.prev

            node.prev = None
            node.next = self.head

            self.head.prev = node
            self.head = node
        elif node == self.head:
            return
        else:
            if node.prev:
                node.prev.next = node.next

            if node.next:
                node.next.prev = node.prev

            node.prev = None

            node.next = self.head
            self.head.prev = node
            self.head = node

        return

    def get(self, key: int) -> int:
        """
        - Get the node, return -1 if not there
        - If exists, update it
        """
        if key not in self.tracker:
            return -1
        
        node = self.tracker[key]
        self.__update_node(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        """
        - check if full
            - if full, delete node
        - populate
        - update node
        """
        delete_flag = False
        if key not in self.tracker and len(self.tracker) == self.capacity:
            print("DELETE Node", key)
            self.__delete_node()

        node = self.tracker.get(key, Node(value, key))
        self.tracker[key]=node
        node.val = value
        self.__update_node(node)