# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
- If values match, match sub tree
- else we do the same for lef tnode and right node

"""

class Solution:   
        
    def __check_tree(self, parent_node, child_node):
        if not parent_node and not child_node:
            return True
        if parent_node and child_node:
            return (parent_node.val == child_node.val) and self.__check_tree(parent_node.left, child_node.left) and self.__check_tree(parent_node.right, child_node.right)

        return False

        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root and subRoot:
            if root.val == subRoot.val and self.__check_tree(root, subRoot):
                return True

            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return False