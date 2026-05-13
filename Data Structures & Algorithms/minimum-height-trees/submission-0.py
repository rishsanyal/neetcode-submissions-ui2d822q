class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        We could do a BFS for all nodes
        Assuming no cycles because Tree
        
        - We could track the distance between origin and edges and use that to memoize a bit
            - we know the distance between edges and the distance between an origin to a node
        - track all MHTs in a dict and get the min later

        Each node can have the following heights to a leaf
        - length between it and one child's leaf

        0 - 1 - 3 - 2
            |
            4

        We could iterate from the nodes with the least amount of connections and go from there
        graph -> heap -> bfs

        {
            0: [1],
            2: [3]
            4: [1],
            3: [1, 2],
            1: [0, 4, 3],
        }

        {
            1: [0],
            2: [0],
            3: [0],
            0: [1, 2, 3]
        }

        set of the min connections
        """

        if n == 1:
            return [0]

        if n == 2:
            return [0, 1]

        graph = defaultdict(set)
        l = {}

        # We have to make the graph
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

            l[a] = len(graph[a])
            l[b] = len(graph[b])

        h = []
        for node, len_children in l.items():
            heapq.heappush(h, (len_children, node))
        
        min_nodes_len = h[0][0]

        res = set()

        while h and h[0][0] == min_nodes_len:
            _, curr_node = heapq.heappop(h)
            res |= graph[curr_node]

        return(list(res))