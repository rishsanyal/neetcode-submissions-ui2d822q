# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        we maintain a counter as we iterate through the nodes

        we go to node.left
        we check current node
        we go to node.right
        """

        self.ctr = 0
        self.res = None

        def __helper(node):
            if not node:
                return
            
            if self.res:
                return

            __helper(node.left)

            self.ctr += 1

            if self.ctr == k:
                self.res = node
                return

            __helper(node.right)


        __helper(root)

        return self.res.val if self.res else None
