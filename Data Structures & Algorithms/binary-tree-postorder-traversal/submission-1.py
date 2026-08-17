# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []


        def __helper(node):
            if not node:
                return

            __helper(node.left)
            __helper(node.right)
            res.append(node.val)

        __helper(root)

        return res