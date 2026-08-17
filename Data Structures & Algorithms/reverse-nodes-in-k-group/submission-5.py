# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
What happens if list is smaller than K? - We leave the list as is

We could reverse K nodes, then connect them, so on

- check K nodes from a node
- If True, get reverse them until K is reached, return curr_head and next node
- link previous node to curr head and curr tail to next node
- repeat

def reverse(node) -> curr_head, curr_tail

"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        head_node = ListNode()
        head_node.next = head

        def check_node_length(node):
            node_head = node
            count = 1

            while count < k and node_head.next:
                count += 1
                node_head = node_head.next

            return (count == k)

        def reverse(node):
            prev = None
            temp_head = node
            count = 0

            while temp_head and count < k:
                temp = temp_head.next
                temp_head.next = prev

                prev = temp_head
                temp_head = temp

                count += 1

            return prev, node, temp_head

        curr_head = head_node.next
        prev_head = head_node

        while curr_head and check_node_length(curr_head):
            h, t, next_head = reverse(curr_head)
            prev_head.next = h

            t.next = next_head
            curr_head = next_head

            prev_head = t


        return head_node.next
        