# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        We could split the list in 3 parts
        0:l, l:r+1, r+1

        We could get the node number recursively
        if number == r:
            we start reversing

        if number == l:
            we stop reversing?

        That's weird, let's scrap that

        find l and r
        we split the list
        reverse from r
        join the lists
        """

        if not head:
            return None

        # prev_node, left, right, after
        nodes = [None, None, None, None]

        res = temp_head = ListNode()
        temp_head.next = head

        def __getList(prev_node, node, curr_count=0):
            if not node:
                return 0

            curr_num = curr_count + 1

            if curr_num == left:
                nodes[0] = prev_node
                nodes[1] = node

            if curr_num == right:
                nodes[2] = node
                nodes[3] = node.next
            
            __getList(node, node.next, curr_count + 1)

            return curr_num

        def __reverse(node):
            if not node:
                return None, None

            prev = None
            curr = node

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev



        __getList(temp_head, temp_head.next)

        left_cut, left_node, right_node, right_cut = nodes

        left_cut.next = None
        right_node.next = None

        left_cut.next, last_node = __reverse(left_node), left_node
        last_node.next = right_cut


        return res.next




