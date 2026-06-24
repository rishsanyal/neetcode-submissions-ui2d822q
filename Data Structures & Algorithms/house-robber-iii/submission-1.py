# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
At each level we have these options
- We pick current node (if we can)
- We skip current node (in both cases)

We check the max loot returned at each level and return that

at each level, we return max possible loot. we can get

def traverse(node, can_select=True):
    if not node:
        return 0

    if can_select:
        options = max(
            node.val + traverse(node.left, False),
            node.val + traverse(node.right, False),
            traverse(node.right, True),
            traverse(node.left, True)
        )
    else:
        options = max(
            traverse(node.right, True),
            traverse(node.left, True)
        )

    return options
"""

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, can_select=True):
            if not node:
                return 0

            if can_select:
                options = max(
                    node.val + traverse(node.left, False),
                    node.val + traverse(node.right, False),
                    traverse(node.right, True),
                    traverse(node.left, True),
                    traverse(node.left, True) + traverse(node.right, True)
                )
            else:
                options = max(
                    traverse(node.right, True),
                    traverse(node.left, True),
                    traverse(node.left, True) + traverse(node.right, True)
                )

            return options

        return traverse(root)

        