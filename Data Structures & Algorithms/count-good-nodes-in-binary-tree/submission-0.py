# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        At each level, we track the max number seen so far
        we have a global counter to track the result
        if a node's good, increment the counter
        """

        res = 0

        def __helper(node, curr_max_val):
            nonlocal res

            if not node:
                return None

            if node.val >= curr_max_val:
                res += 1
            
            __helper(node.left, max(node.val, curr_max_val))
            __helper(node.right, max(node.val, curr_max_val))

            return None

        __helper(root, float('-inf'))

        return res