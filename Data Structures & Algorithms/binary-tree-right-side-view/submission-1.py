# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
BFS - Queue
DFS - Stack

We could pick up only the last ones on every level, if we do a BFS

BFS - Everytime the queue is empty, we append to result
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
            
        res = []
        itr = [root]
        temp = []

        while itr:
            curr_node = itr.pop(0)

            if curr_node.left:
                temp.append(curr_node.left)
            if curr_node.right:
                temp.append(curr_node.right)

            if not itr:
                res.append(curr_node.val)
                itr, temp = temp, itr

        return res
                

            
        