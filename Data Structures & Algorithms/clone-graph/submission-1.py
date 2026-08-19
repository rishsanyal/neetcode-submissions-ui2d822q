"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


- Track Nodes in a dict by values
- If we haven't seen one, we create it
- We could (DFS) recursively go through all the nodes and keep creating them


tracker = {node_value: NewCreatedNode()}

helper(input_node):
    if input_node.val not in tracker:
        new_node = NewNode()
        tracker[new_node] = new_node

        for n in input_node.neighbors:
            new_node.neighbors.append(
                __helper(n)
            )
    else:
        new_node = tracker[new_node]

    return new_node
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        tracker = {}

        def __helper(input_node):
            if not input_node:
                return None
                
            if input_node.val not in tracker:
                tracker[input_node.val] = Node(input_node.val)
                new_node = tracker[input_node.val]

                for n in input_node.neighbors:
                    new_node.neighbors.append(
                        __helper(n)
                    )
            else:
                new_node = tracker[input_node.val]

            return new_node

        return __helper(node)

        