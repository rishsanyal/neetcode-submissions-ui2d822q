# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Root stays the same
we invert left and right
then go deeper into them


"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            if node:
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)
            return node

        return invert(root)