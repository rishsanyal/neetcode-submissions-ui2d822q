"""
We could have multiple elements per key? NO
1 key - 1 element
0 <= key, value <= 1,000,000

We coudl actually implement a hashmap
- An array with a hash function


Hashing Collisions:
- Open Addressing - Find the next free spot
- Chaining - Use a linked list
    - With chaining how do we know which key we're looking at? We iterate through the linkedlist node

"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:

    def __init__(self):
        self.tracker = [None] * 1_000_001

    def put(self, key: int, value: int) -> None:
        self.tracker[key] = value

    def get(self, key: int) -> int:
        return self.tracker[key] or -1

    def remove(self, key: int) -> None:
        self.tracker[key] = None

    def __hash_func(self, key):
        return key % 1_000_000
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)