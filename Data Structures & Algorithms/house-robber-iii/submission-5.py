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

        cache = {None: 0}
        
        def traverse(node):
            if node in cache:
                return cache[node]

            cache[node] = node.val

            if node.left:
                cache[node] += traverse(node.left.left) + traverse(node.left.right)
            if node.right:
                cache[node] += traverse(node.right.left) + traverse(node.right.right)

            cache[node] = max(cache[node], traverse(node.left) + traverse(node.right))

            return cache[node]

        return traverse(root)

        