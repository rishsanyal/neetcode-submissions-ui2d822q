# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        THEY'RE NODES
        WE CAN STORE ALL OF THEM IN A HEAP and IT'LL TAKE O(K) SPACE
        """

        h = []
        curr_node = head = ListNode()

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))

        while h:
            val, i, node = heapq.heappop(h)

            curr_node.next = ListNode(val)
            curr_node = curr_node.next
            
            node = node.next

            if node:
                heapq.heappush(h, (node.val, i, node))

        return head.next



# class Solution:   
#     def mergeKLists(self, lists):
#         h = []
#         head = curr = ListNode()

#         # Push first node from each list
#         for i, node in enumerate(lists):
#             if node:
#                 heapq.heappush(h, (node.val, i, node))

#         while h:
#             val, i, node = heapq.heappop(h)
#             curr.next = node
#             curr = curr.next

#             # Advance that list and push its next node
#             if node.next:
#                 heapq.heappush(h, (node.next.val, i, node.next))

#         return head.next