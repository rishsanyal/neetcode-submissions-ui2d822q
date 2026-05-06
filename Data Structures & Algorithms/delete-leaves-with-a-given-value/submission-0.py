# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        we go to the node's children first and delete them if they're equal to the value
        then we check the parent and do the same
        """

        def __helper(node):
            if not node:
                return None

            node.left = __helper(node.left)
            node.right = __helper(node.right)

            if not (node.left or node.right) and node.val == target:
                return None
            
            return node

        root = __helper(root)

        return root
