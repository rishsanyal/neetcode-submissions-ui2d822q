# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        - We switch the value with the left child and delete the left child
        - We switch the value with the right child and delete the right child
        """

        if not root:
            return None

        if root.val == key:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            curr = root.right
            while curr.left:
                curr = curr.left

            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root