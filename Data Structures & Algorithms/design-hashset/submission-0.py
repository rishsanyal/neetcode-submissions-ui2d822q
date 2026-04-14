"""
Use a linkedlist and we could go through the list to check for existence of elements

- Sorted linkedlist? NO
- Look at the constraints
    - At most 1,000,000
    - We're implementing a hash SET - one of each
"""
# class Node:
#     def __init__(self, val=None):
#         self.next = None
#         self.val = val

class MyHashSet:

    def __init__(self):
        self.tracker = [False] * 1_000_000

    def add(self, key: int) -> None:
        self.tracker[key] = True

    def remove(self, key: int) -> None:
        self.tracker[key] = False

    def contains(self, key: int) -> bool:
        return self.tracker[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)