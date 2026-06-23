# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We use 2 different lists, one to hold and another as result
we append to result when holding is empty
and then replace them

level, itr, next_nodes
[], [4,5,6,7], []
  
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

            return
        
        dfs(root, 0)

        return res