# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
at every level, we get the height
return the max height from that node + 1

"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def __helper(node):
            nonlocal balanced

            if not node:
                return 0

            left_h = __helper(node.left)
            right_h = __helper(node.right)

            if abs(left_h - right_h) > 1:
                balanced = False

            return 1 + max(left_h, right_h)

        __helper(root)

        return balanced