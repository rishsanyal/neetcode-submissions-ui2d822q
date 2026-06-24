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

            result = 0

            if not node:
                return result

            if node in cache:
                return cache[node]

            if (not node.left) and (not node.right):
                result = node.val
            elif node.left and not node.right:
                result = max(
                    node.val + traverse(node.left),
                    node.val
                )
            elif node.right and not node.left:
                result = max(
                    node.val + traverse(node.right),
                    node.val
                )
            else:
                result = max(
                    node.val + traverse(node.right),
                    node.val + traverse(node.left),
                    traverse(node.right) + node.val + traverse(node.left),
                    node.val
                )

            res = max(
                result,
                res
            )

            cache[node] = result

            return max(0, result)


        traverse(root)

        return res