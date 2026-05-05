# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BST but when the  list is empty, we add to result
            we maintain a temp list, to replace the list we're iterating through
                the iteration list will be empty between levels.

        we start with [root]
        root.pop -> makes list empty, so we know that we've finished a level.

        Issues like, unbalanced tree, empty tree won't affect this.
        """
        res = []
        if not root:
            return res

        itr = [root]
        temp_val = []
        next_nodes = []

        while itr:
            curr_node = itr.pop(0)
            temp_val.append(curr_node.val)

            if curr_node.left:
                next_nodes.append(curr_node.left)
            if curr_node.right:
                next_nodes.append(curr_node.right)

            if not itr:
                res.append(temp_val.copy())
                temp_val = []

                next_nodes, itr = itr, next_nodes

        return res
