
"""
We can make our own nodes
- Doubly linkedList
- Hash for values


On every get or put, we need to take the node out and put it in the front of the linkedlist
- How do we avoid getting O(N) time for the last node?
- We track the tail value in the class - Everytime we remove the tail, we replace it with the previous Node
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
        key = self.tail.key

        self.tracker.pop(key)

        self.tail = self.tail.prev
        self.tail.next = None

    def __update_node(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return

        prev_node = node.prev
        next_node = node.next

        if prev_node:
            prev_node.next = next_node
        
        if next_node:
            next_node.prev = prev_node

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
        if key not in self.tracker:
            delete_flag = len(self.tracker) == self.capacity

        node = self.tracker.get(key, Node(value, key))
        self.tracker[key]=node

        if delete_flag:
            self.__delete_node()

        self.__update_node(node)