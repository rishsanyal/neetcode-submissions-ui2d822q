class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        What makes a valid tree?
        - No cycles
            - we need to make sure we don't go in reverse too but need to track cycles
        - all nodes are connected - so we start from 0

        Check for cycles with DFS

        we could use a DFS and mark nodes as visited as we go on
        we could use a set of edges and keep popping paths off that as we traverse
        after we're done iterating we remove the opposite edge from the set and from the graph?

        we still need to track if they're all connected, we do that by having a global visited set
        """

        # Make the graph
        graph = defaultdict(set)

        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        global_v = set()

        def dfs(curr_v, origin_v=None):
            nonlocal global_v

            if curr_v in global_v:
                return False

            global_v.add(curr_v)

            for child in graph.get(curr_v, set()):
                if curr_v in graph[child]:
                    graph[child].remove(curr_v)

                if not dfs(child, curr_v):
                    return False

            return True

        # We just need to start from one because it's a tree
        return dfs(0) and len(global_v) == n

        

