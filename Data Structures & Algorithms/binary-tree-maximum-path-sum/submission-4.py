# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Do we have negative numbers? - YES

We need the option of skipping Nodes? - We can't skip them we need a 
    subarray equivalent of binary tree

At every point we need the following:
- curr node value
- max path on left
- max path on right



"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float('-inf')
        cache = {}

        def traverse(node):
            nonlocal res

            if node is None:
                return 0

            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)

            res = max(
                res,
                left + node.val + right,
                node.val
            )
            
            return node.val + max(left, right)


        traverse(root)

        return res