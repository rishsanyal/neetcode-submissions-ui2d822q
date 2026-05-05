# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        We always insert as a leaf
        So we iterate until we get a leaf - Absolute spot where it can be inserted in

        For iteration:
            - Go left if less
            - go right if more
            - keep going until we hit an empty space
        """

        def traverse(node):
            if val < node.val:
                if node.left:
                    traverse(node.left)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    traverse(node.right)
                else:
                    node.right = TreeNode(val)

            return node

        if root:
            return traverse(root)

        return None
