# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        We need 2 things, node and curr height
        as we iterate, we increase the height
        Let's use a single, funciton level variable to track
        """

        res = 0

        def traverse(node, height):
            if node:
                return max(
                    traverse(node.left, height+1),
                    traverse(node.right, height+1),
                    height
                )
            
            return 0

        return traverse(root, 1)