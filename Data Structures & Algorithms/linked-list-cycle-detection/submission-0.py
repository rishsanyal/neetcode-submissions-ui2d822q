# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return True

        slow_ptr, fast_ptr  = head, head.next

        while slow_ptr and fast_ptr and slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next if fast_ptr.next else fast_ptr.next

        return slow_ptr == fast_ptr

        
        