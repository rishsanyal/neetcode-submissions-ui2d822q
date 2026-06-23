# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- We find p or q first: That's the result
- p and q are lesser than node
- p and q are greater than node
- we have the answer
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def traverse(node):
            if not node:
                return None

            if p.val < node.val and q.val < node.val:
                return traverse(node.left)
            elif p.val > node.val and q.val > node.val:
                return traverse(node.right)
            elif p.val == node.val or q.val == node.val:
                return p if p.val == node.val else q

            return node

        return traverse(root)
