# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
- Split the list in 2
    - slow ptr and fast ptr
- reverse the latter list
- join alternatively

"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow_ptr, fast_ptr = head, head.next

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next

            if fast_ptr.next:
                fast_ptr = fast_ptr.next.next
            else:
                fast_ptr.next

        first_list = head
        latter_list = slow_ptr.next

        slow_ptr.next = None

        def reverse(node):

            curr_head = node
            prev = None

            while curr_head:
                temp = curr_head.next
                curr_head.next = prev

                prev = curr_head
                curr_head = temp

            return prev

        latter_list = reverse(latter_list)

        res = ListNode()
        h = res

        while first_list and latter_list:
            temp1, temp2 = first_list.next, latter_list.next

            first_list.next = None
            latter_list.next = None

            h.next = first_list
            h.next.next = latter_list

            h = h.next.next

            first_list = temp1
            latter_list = temp2
        
        if first_list:
            h.next = first_list

        if latter_list:
            h.next = latter_list

        