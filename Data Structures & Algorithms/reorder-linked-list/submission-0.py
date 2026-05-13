# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        we could split the list into two halves and rejoin it after reverseing the second half
        """

        if not head:
            return None

        def __reverse(curr):
            prev = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev


        slow, fast = head, head.next
        res = res_head = ListNode()

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec_half = slow.next
        slow.next = None

        sec_half = __reverse(sec_half)

        # while sec_half:
        #     print(sec_half.val)
        #     sec_half = sec_half.next

        while head or sec_half:
            if head:
                res_head.next = head
                head = head.next

                res_head = res_head.next
            
            if sec_half:
                res_head.next = sec_half
                sec_half = sec_half.next

                res_head = res_head.next


        return res_head.next