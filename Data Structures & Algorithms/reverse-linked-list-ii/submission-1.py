# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

- We attach the head to temporary Node to track the result
- We start counting from there
    - we keep reversing until the next node is None or right+1
- We then link the list's nodes


Edge cases:
1. Invalid number(s)
2. Cycles
3. Invalid List
"""



class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:


        def print_list(head_node):
            temp = head_node

            while temp:
                print(temp.val)
                temp = temp.next


        res = ListNode()
        res_head = res
        res_head.next = head

        left_node = res_head
        left_node_ctr = 0

        initial_list_tail = None

        while left_node_ctr < left:
            initial_list_tail = left_node

            left_node = left_node.next
            left_node_ctr += 1

        initial_list_tail.next = None

        # print_list(res_head.next)

        right_node = left_node
        right_node_ctr = left_node_ctr

        while right_node_ctr < right:
            right_node = right_node.next
            right_node_ctr += 1

        rest_list = right_node.next
        right_node.next = None

        # We have left node and right node
        def __reverse(node_head):
            prev = None
            curr_head = node_head
            new_head = None

            while curr_head:
                temp = curr_head.next
                curr_head.next = prev

                prev = curr_head
                curr_head = temp

            return prev

        new_head = __reverse(left_node)
        
        initial_list_tail.next = new_head

        while initial_list_tail.next:
            initial_list_tail = initial_list_tail.next
        
        initial_list_tail.next = rest_list

        return res_head.next

        






        
        