class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        What makes a valid tree?
        - No cycles
        - all nodes exist/ are connected
        - we need to check if all nodes have 1 incoming edge
        - we need to make sure we don't go in reverse too but need to track cycles

        Check for cycles with DFS
        we can check if there's only 1 edge incoming and 1 outgoing
            - with a visited set


        we could use a DFS and mark nodes as visited as we go on
        we could use a set of edges and keep popping paths off that as we traverse
        after we're done iterating we remove the opposite edge from the set and from the graph?
        """

        # Make the graph
        graph = defaultdict(set)

        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        global_v = set()

        def dfs(curr_v, visited, origin_v=None):
            nonlocal global_v

            global_v.add(curr_v)

            if curr_v in visited:
                return False

            visited.add(curr_v)

            for child in graph.get(curr_v, set()):
                if curr_v in graph[child]:
                    graph[child].remove(curr_v)

                if not dfs(child, visited, curr_v):
                    return False

            visited.remove(curr_v)

            return True

        if not dfs(0, set()):
            return False

        return True and len(global_v) == n

        

