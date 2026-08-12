# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
We get the number of node
we pass previous node and connect it to the next node if the number matches
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        prev_node = ListNode()
        prev_node.next = head

        def check_node(prev_node, curr_node):
            if curr_node is None:
                return 1

            curr_num = check_node(curr_node, curr_node.next)

            if curr_num == n:
                prev_node.next = curr_node.next if curr_node else None

            return curr_num + 1

        check_node(prev_node, prev_node.next)

        return prev_node.next


