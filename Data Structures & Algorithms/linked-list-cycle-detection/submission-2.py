# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        slow_ptr, fast_ptr  = head, head.next

        while fast_ptr and fast_ptr.next and slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr == fast_ptr

        
        