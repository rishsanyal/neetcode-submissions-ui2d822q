# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        We need to track the carried number over here. That's the important part

        9-9
        9-9
        8-9-1


        """


        carry_num = 0
        res = res_head = ListNode()

        while l1 and l2:
            curr_num = carry_num + l1.val + l2.val
            carry_num = curr_num // 10
            curr_num = curr_num % 10

            res.next = ListNode(curr_num)
            res = res.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            curr_num = carry_num + l1.val
            carry_num = curr_num // 10
            curr_num = curr_num % 10

            res.next = ListNode(curr_num)
            res = res.next

            l1 = l1.next


        while l2:
            curr_num = carry_num + l2.val
            carry_num = curr_num // 10
            curr_num = curr_num % 10

            res.next = ListNode(curr_num)
            res = res.next

            l2 = l2.next

        if carry_num:
            res.next = ListNode(carry_num)
            res = res.next

        return res_head.next
