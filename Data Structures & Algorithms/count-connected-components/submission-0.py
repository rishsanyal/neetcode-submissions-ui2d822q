class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Number of connected components in a graph
        We could do BFS and gather all visited nodes and mark them with 1 ID

        It's undirected though, so we'll have to track which nodes we've previously visited.

        Why is disjoint set better?

        BFS:
        We'll visit every connected node here
        - create graph
        - iterate from nodes with a counter and for every node we encounter, we add to a set
        - we add all entries from that set to a hashmap with the counter
        - increase the counter if the number doesn't exist in the hashmap
        """

        node_tracker = {}
        graph = defaultdict(set)
        ctr = 0

        for (i,j) in edges:
            graph[i].add(j)
            graph[j].add(i)

        def bfs(node, visited):
            if node in visited:
                return

            if node in node_tracker:
                return
            
            node_tracker[node] = ctr

            visited.add(node)

            for child in graph[node]:
                if child == node:
                    continue
                bfs(child, visited)

            visited.remove(node)

            return

        for i in range(n):
            if i not in node_tracker:
                ctr += 1
                bfs(i, set())

        return ctr
