# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def __helper(node, curr_list):
            if not node:
                return None
            
            self.inorderTraversal(node.left)
            curr_list.append(node.val)
            self.inorderTraversal(node.right)

        res = []
        __helper(root, res)

        return res