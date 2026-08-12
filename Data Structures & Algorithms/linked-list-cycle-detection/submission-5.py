# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr = head
        fast_ptr = head.next

        while fast_ptr and slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next

            if fast_ptr.next:
                fast_ptr = fast_ptr.next.next
            else:
                return False

        return (fast_ptr == slow_ptr)