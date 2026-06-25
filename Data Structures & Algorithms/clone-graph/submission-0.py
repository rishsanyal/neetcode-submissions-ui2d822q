"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        - lookup
        We have a dict with nodes
        We then iterate through the node and it's neighbors

        We iterate through a node
        if it exists in a dict, use that node
        else: create node, iterate through it and it's neighbors

        DFS
        """
        node_dict = {}

        def __helper(node):
            if node in node_dict:
                return node_dict[node]

            if not node:
                return None

            node_dict[node] = Node(node.val)

            for neighbor in node.neighbors:
                node_dict[node].neighbors.append(__helper(neighbor))

            return node_dict[node]

        return __helper(node)
