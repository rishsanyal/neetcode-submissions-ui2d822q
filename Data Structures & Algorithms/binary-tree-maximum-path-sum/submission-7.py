# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res

            if node is None:
                return 0

            result = node.val

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            result = max(node.val, node.val + max(left, right))

            res = max(res, result, left + node.val + right)

            return result

        dfs(root)

        return res