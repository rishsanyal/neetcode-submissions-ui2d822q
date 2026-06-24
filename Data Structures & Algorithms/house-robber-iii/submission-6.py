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
