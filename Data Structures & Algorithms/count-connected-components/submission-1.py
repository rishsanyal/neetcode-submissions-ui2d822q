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
        graph = defaultdict(list)
        ctr = 0

        for (i,j) in edges:
            graph[i].append(j)
            graph[j].append(i)

        def bfs(node):
            node_tracker[node] = ctr

            children = deque(graph.get(node, []))

            while children:
                child = children.popleft()
                nodes = graph.get(child, [])

                for child_node in nodes:
                    if child_node not in node_tracker:
                        children.append(child_node)

                node_tracker[child] = ctr

            return

        for i in range(n):
            if i not in node_tracker:
                ctr += 1
                bfs(i)

        return ctr
