# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        we get the number once we hit the end of the linkedlist

        we track prev node, curr_node

        we keep going until we get the number of the node == n
        we link the prev node and next node when node number == n
        """


        def returnCount(prev_node, node):
            if not node:
                return 0

            curr_count = 1 + returnCount(node, node.next)

            if curr_count == n:
                prev_node.next = node.next

            return curr_count

        res = ListNode()
        res.next = head
        returnCount(res, res.next)

        return res.next
