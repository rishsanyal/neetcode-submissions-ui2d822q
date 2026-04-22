# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We compare each node
if any node is not equal, we stop iterating
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True

        def traverse(l, r):
            nonlocal res

            if not res:
                return False

            if l is None and r is None:
                return res
            
            elif (l is None) or (r is None):
                res = False
                return False
            
            left_status = traverse(l.left, r.left)
            right_status = traverse(l.right, r.right)

            res = (l.val == r.val) and left_status and right_status and res

            return res

        return traverse(p, q)

        