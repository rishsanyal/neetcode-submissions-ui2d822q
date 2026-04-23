# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if p.val > q.val:
            p, q = q, p

        def find(node):
            if node:
                if p.val < q.val < node.val:
                    return find(node.left)
                elif node.val < p.val < q.val:
                    return find(node.right)
                else:
                    return node
            return None

        return find(root)