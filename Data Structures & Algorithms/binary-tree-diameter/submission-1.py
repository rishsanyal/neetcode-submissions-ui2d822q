# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
The answer is one of three
longest left path
longest right path
sum of longest left path and longest right path

base case -> no node, return 0

get left height
get right height

ans could also be both, so update that result too

return max(left height, right height)
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def traverse(node):
            nonlocal res
            if node:
                left_length = traverse(node.left)
                right_length = traverse(node.right)

                result = max(left_length, right_length)
                res = max(result, right_length + left_length, res)
                return 1 + result

            return 0
        
        traverse(root)
        return res
