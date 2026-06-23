# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

helper(node, curr_count):
if curr_count == k:
    reverse k nodes

No because it's a singly linked list
we could track current node and then go from there?

we get current node
we check if k nodes exist
- if they do: reverse them and set curr_node.next, last_node = reverse_k_nodes(curr_node.next)
- recurse(last_node)



"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def check_nodes(node, curr_count):
            if node is None:
                return (k - curr_count == 0)

            if k == curr_count:
                return True, node
            else:
                return check_nodes(node.next, curr_count + 1)

        def reverse_nodes(node):
            curr_node = node
            curr_count = 0

            new_head, new_tail = None, node

            prev_node = None

            # We have to reverse k nodes
            while curr_count < k and curr_node:
                next_node = curr_node.next
                
                curr_node.next = prev_node
                prev_node = curr_node
    
                new_head = curr_node

                curr_node = next_node

                curr_count += 1


            return new_head, new_tail
         
        def helper(node, curr_count):
            if node is None:
                return None

            # check for the next k-curr_count nodes
            nodes_exist, temp_node = check_nodes(node, curr_count)
            

            if nodes_exist:
                next_head, node = reverse_nodes(node)
                node.next = helper(node.next, 0)

            return next_head

        
        return helper(head, 0)