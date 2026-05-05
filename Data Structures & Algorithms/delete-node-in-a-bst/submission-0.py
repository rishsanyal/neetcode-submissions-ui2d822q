# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Easily done recursively.

            There's 3 cases:
            1. No child: No problem
            2. 1 child: next highest number
                what if there's no highest number only low numbers?
                then closest number -> Left node
            3. 2 children
                Next highest number

            Steps:
            1. We find the node's parent?
                on every level we return to_be_deleted, node
            2. If no child, we delete the node
            3. If 2 children, find the max and move it
            4. if 1 child, find the closest and return that
        """

        def __helper(curr_node, val):
            if not curr_node:
                return None

            if curr_node.val < val:
                curr_node.right = __helper(curr_node.right, val)
            elif curr_node.val > val:
                curr_node.left = __helper(curr_node.left, val)
            else:
                if curr_node.left and curr_node.right:
                    curr_min = curr_node.right

                    while curr_min and curr_min.left:
                        curr_min = curr_min.left

                    curr_node.val = curr_min.val
                    curr_node.right = __helper(curr_node.right, curr_min.val)

                elif (not curr_node.right) and curr_node.left:
                    curr_node.val = curr_node.left.val
                    curr_node.left = __helper(curr_node.left, curr_node.left.val)
                elif (not curr_node.left) and curr_node.right:
                    curr_node.val = curr_node.right.val
                    curr_node.right = __helper(curr_node.right, curr_node.right.val)
                else:
                    curr_node = None

            return curr_node

        __helper(root, key)

        return root



