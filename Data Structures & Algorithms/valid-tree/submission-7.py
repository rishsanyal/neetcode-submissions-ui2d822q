"""

Tree conditions:
1. No cycles
2. All nodes are connected

- We track all outgoing edges (in a dict)
- DFS through each while tracking the previoulsy seen nodes
- If cycle, return False

- We don't need a global seen here. Cycles will show up

the edges are undirected 
    - we can mark invalid edges as we go on
    - we can remove the parent from the nodes as we go on
    - We just need to not go to the parent back [X]

0 - [1,2,3]
1 - [4], (0)
4 - [], (0, 1)
2 - [], (0)
3 - [], (0)

0 - [1]
1 - [4,2,3] {0}
4 - [], {0, 1}
2 - [3], {0, 1}
3 - [1], {0, 1, 2} - CYCLE

"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        dependencies = defaultdict(set)
        global_visited = set()

        for a,b in edges:
            dependencies[a].add(b)
            dependencies[b].add(a)


        def __helper(curr_node, parent_node, seen):

            seen.add(curr_node)

            for node in dependencies.get(curr_node, set()):
                if node == parent_node or node in global_visited:
                    continue

                if node in seen:
                    return False

                child_s = __helper(node, curr_node, seen)
                
                if not child_s:
                    return False

            global_visited.add(curr_node)
            return True

        
        s = __helper(0, None, set())

        return len(global_visited) == n