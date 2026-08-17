# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr_list = []
        def __helper(node):
            if node is None:
                return
            
            __helper(node.left)
            curr_list.append(node.val)
            __helper(node.right)

        __helper(root)

        return curr_list