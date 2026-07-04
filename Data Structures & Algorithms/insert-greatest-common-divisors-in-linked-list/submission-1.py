# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Calculating  Greatest Common Divisors

we start from the larger number 

bigger_number = (smaller_number * q) + r
4 = 3*1 + 1
3 = 1*3 + 0

10 = 6*1 + 4
6 = 4*1 + 2
4 = 2*2 + 0

We can have a helper function to return GCD

we use 2 nodes, we can create a different linked-list with each of the GCD's

we join them in the end
"""

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        gcd_list_head = ListNode()
        gcd_list = gcd_list_head

        curr_node = head
        head_node = head

        def __helper(num_1, num_2):
            while num_2 != 0:
                num_1, num_2 = num_2, num_1 % num_2
            return num_1


        # print(__helper(12,3))
        # print(__helper(4,3))
        # print(__helper(4,6))
        print(__helper(6,10))

        while curr_node and curr_node.next:
            # save the next node
            next_node = curr_node.next

            # Get the numbers
            curr_num = curr_node.val
            next_num = next_node.val

            # Get the 
            gcd = ListNode(__helper(curr_num, next_num))

            curr_node.next = gcd
            gcd.next = next_node

            curr_node = next_node

        return head_node
        