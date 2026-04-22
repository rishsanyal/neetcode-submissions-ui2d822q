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

        res = True

        def getHeight(node):
            nonlocal res
            if node and res:
                left_height = getHeight(node.left)
                right_height = getHeight(node.right)

                res = (abs(right_height - left_height) <= 1)

                return 1 + max(left_height, right_height)

            return 0
        
        getHeight(root)

        return res