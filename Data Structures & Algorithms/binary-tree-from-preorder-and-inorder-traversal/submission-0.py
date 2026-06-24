# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_indices = {val: idx for (idx, val) in enumerate(inorder)}
 
        def __helper(preorder_list):
            nonlocal inorder_indices

            if not preorder_list:
                return None

            node = TreeNode(preorder_list.pop(0))

            node.left = __helper(preorder_list[:inorder_indices[node.val]])
            node.right = __helper(preorder_list[inorder_indices[node.val]+1:])

            return node

        return __helper(preorder)
            