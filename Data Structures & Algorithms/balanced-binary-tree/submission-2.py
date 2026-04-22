# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"We have to return the max of left tree or right tree and then check fi it differs by 1"

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def getHeight(node):
            if node:
                left_height = getHeight(node.left)
                right_height = getHeight(node.right)

                return 1 + max(left_height, right_height)

            return 0

        if not root.left and root.right:
            return getHeight(root.right) <= 1
        if not root.right and root.left:
            return getHeight(root.left) <= 1
        if not root.right and not root.left:
            return True

        return (abs(getHeight(root.left) - getHeight(root.right)) <= 1)