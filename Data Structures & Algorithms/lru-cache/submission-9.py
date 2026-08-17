"""
- Use a dict to track key: value
- Use a linkedlist to track the order of operations

- have a head and tail

- Key is considered used if get or put is called
- Each operation should be O(1)
- we find the node and re-insert it
- with a DOUBLY LINKED LIST we can track the end and re-populate it when we need to

Can we do this with a singly linked list?
- becomes trickier, not sure if it's worth

"""

class ListNode:
    def __init__(self, key=0, val=0) -> None:
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tracker = {}
        self.list_head = ListNode()
        self.list_tail = ListNode()

        self.list_tail.prev = self.list_head
        self.list_head.next = self.list_tail

    def __print_node(self, node):
        print("-#-"*10)

        temp = node
        while temp:
            print(temp.key)
            print(temp.val)
            temp = temp.next

        print("-#-"*10)

        print(self.tracker)

    def get(self, key: int) -> int:
        if key in self.tracker:
            node = self.tracker[key]
            self.insert(node)

            return node.val

        # print('Not in tracker GET ', key)
        return -1

    def insert(self, node):
        existing = False

        if node.prev and node.next:
            existing = True

        if existing:
            node.next.prev = node.prev
            node.prev.next = node.next

            node.prev = None
            node.next = None

        curr_head = self.list_head.next

        curr_head.prev = node
        self.list_head.next = node

        node.prev = self.list_head
        node.next = curr_head

        return None

    def put(self, key: int, value: int) -> None:
        if key in self.tracker:
            self.tracker[key].val = value
        else:
            if len(self.tracker) == self.capacity:
                curr_tail = self.list_tail.prev

                curr_tail.prev.next = curr_tail.next
                curr_tail.next.prev = curr_tail.prev

                self.tracker.pop(curr_tail.key)

            self.tracker[key] = ListNode(key, value)
    
        self.insert(self.tracker[key])

        # self.__print_node(self.list_head)




        


        
