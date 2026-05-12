class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Disjoint Set
        Runtime -> O(V+E) - same as DFS since the union function is constant
        """

        rank = [1] * (len(edges)+1)
        parent = [i for i in range(len(edges)+1)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return False

            r1, r2 = rank[p1], rank[p2]

            if r1 >= r2:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True


        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return []
