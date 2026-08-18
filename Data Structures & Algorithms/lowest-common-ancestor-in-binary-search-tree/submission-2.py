# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
binary search tree (BST) 


"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val > q.val:
            p, q = q, p
        
        if p.val <= root.val <= q.val:
            return root
        if p.val >= root.val and q.val >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val <= root.val and q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return None
        