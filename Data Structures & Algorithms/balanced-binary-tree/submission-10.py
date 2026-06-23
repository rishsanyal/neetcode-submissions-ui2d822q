# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We get the left height and the right height
check the difference and return the value

If at any point the value is -ve, we need to stop iterating and return False
- use a global flag for this.
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Set to true if not balanced
        is_balanced = True

        def traverse(node):
            nonlocal is_balanced

            if not node:
                return 0

            if not is_balanced:
                return 0

            left_height = traverse(node.left)
            right_height = traverse(node.right)

            if (abs(right_height - left_height) > 1):
                is_balanced = False
                return 0

            return 1 + max(left_height, right_height)

        traverse(root)

        return is_balanced

