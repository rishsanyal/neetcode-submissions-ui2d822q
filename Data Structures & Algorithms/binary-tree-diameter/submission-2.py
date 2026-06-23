# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

not node: return 0

Ans is max(
- Longest left + longest right
- 1 + longest left
- 1 + longest right
)

but we return only 
max (
    1 + longest left
    1 + longest right
)
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def traverse(node):
            nonlocal res

            if not node:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            res = max(left+right, left, right, res)
            result = max(left, right)

            return 1 + result


        traverse(root)

        return res