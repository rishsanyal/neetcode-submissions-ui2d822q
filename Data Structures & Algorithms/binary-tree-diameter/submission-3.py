# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We need a global counter
we need to return the length to the parent
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def __helper(node):
            nonlocal res

            if not node:
                return 0

            left_len = __helper(node.left)
            right_len = __helper(node.right)

            curr_longest = max(left_len, right_len)

            print(node.val, left_len, right_len)

            res = max(
                res,
                curr_longest,
                left_len + right_len
            )

            return 1 + curr_longest

        __helper(root)

        return res


            