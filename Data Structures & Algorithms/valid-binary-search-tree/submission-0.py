# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        initMax, initMin = float('inf'), float('-inf')

        def validate(node, maxNum=initMax, minNum=initMin):
            if node:
                if not (minNum < node.val < maxNum):
                    return False

                l = validate(node.left, node.val, minNum)
                r = validate(node.right, maxNum, node.val)

                return l and r
            return True

        return validate(root)

