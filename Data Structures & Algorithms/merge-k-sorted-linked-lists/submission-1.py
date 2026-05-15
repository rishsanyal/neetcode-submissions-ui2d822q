# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        We use a single heap for all K elements
        Track empty indices in a set

        On each iteration we get K elements in the list
        we pop one and and creat a node and keep adding to that node.
        """

        h = []
        curr_node = head = None
        empty_idx = set()

        while lists and len(empty_idx) < len(lists):
            for idx, node in enumerate(lists):
                if node:
                    heapq.heappush(h, node.val)
                    lists[idx] = node.next
                else:
                    empty_idx.add(idx)

            if not h:
                break
                
            if curr_node:
                curr_node.next = ListNode(heapq.heappop(h))
                curr_node = curr_node.next
            else:
                curr_node = ListNode(heapq.heappop(h))


        while h:
            curr_node.next = ListNode(heapq.heappop(h))
            curr_node = curr_node.next

        return head


            








