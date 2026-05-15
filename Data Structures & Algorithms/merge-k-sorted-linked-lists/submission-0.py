# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        We could iterate through all the lists
        1 iterate per len(lists) -> O(N)?

        What if we use a MAX heap of K size? Could be easy
        Store everything in the heap
        """

        import heapq

        h = []
        empty_idx = set()
        temp_node = None

        while lists and len(empty_idx) < len(lists):
            for idx, node in enumerate(lists):
                if node is not None:
                    info = node.val
                    lists[idx] = node.next

                    heapq.heappush_max(h, info)
                else:
                    empty_idx.add(idx)

        while h:
            """
            pop
            create a node
            new node.next = temp
            temp = new node
            """

            num = heapq.heappop_max(h)
            new_node = ListNode(num)
            if temp_node:
                new_node.next = temp_node
            temp_node = new_node

        return temp_node

        


