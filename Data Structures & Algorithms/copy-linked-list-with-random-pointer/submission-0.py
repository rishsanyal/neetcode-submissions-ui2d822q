"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        We need a way to map previous Nodes to New Nodes 
            because the random pointer will point to old nodes
            and we need the new list random pointers to point to the new nodes

        we could map by values IF the values are unique - Let's assume they're not

        we create a map with old nodes
        we iterate through the old head
            get next node from map
                if doesn't exist create it

            get random pointer from map
                if doesn't exist then create it
        """

        node_map = {}

        temp = head
        res = res_head = Node(0)

        while temp:
            node_map[temp] = Node(temp.val)
            temp = temp.next

        temp = head

        while temp:
            res.next = node_map[temp]
            res = res.next

            if temp.next:
                res.next = node_map[temp.next]
            if temp.random:
                res.random = node_map[temp.random]

            temp = temp.next

        return res_head.next





        