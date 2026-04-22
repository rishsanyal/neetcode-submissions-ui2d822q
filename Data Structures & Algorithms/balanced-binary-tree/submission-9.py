class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def traverse(node):
            nonlocal res
            if not node or not res:
                return 0

            l = traverse(node.left)
            r = traverse(node.right)

            res = (abs(l-r) <= 1)

            return 1 + max(l, r)

        traverse(root)

        return res