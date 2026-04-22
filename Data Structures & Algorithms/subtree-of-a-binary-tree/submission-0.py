# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We iterate until we see a similar node
then we compare
"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(l, r):
            if not l and not r:
                return True
            elif not l or not r:
                return False
            elif (l.val == r.val):
                left = compare(l.left, r.left)
                right = compare(l.right, r.right)
                return left and right
            
            return False


        def traverse(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            elif compare(l, r):
                return True

            return traverse(l.left, subRoot) or traverse(l.right, subRoot)

        return traverse(root, subRoot)