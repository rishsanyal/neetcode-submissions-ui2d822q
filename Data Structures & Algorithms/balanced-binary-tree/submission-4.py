# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"We have to return the max of left tree or right tree and then check fi it differs by 1"

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def getHeight(node):
            if node:
                left_height = getHeight(node.left)
                if not left_height[0]:
                    return False, 0

                right_height = getHeight(node.right)
                if not right_height[0]:
                    return False, 0

                res = left_height[0] and right_height[0] and (abs(right_height[1] - left_height[1]) <= 1)

                return (res, 1 + max(left_height[1], right_height[1]))

            return True, 0

        curr_res = getHeight(root)[0]

        return curr_res