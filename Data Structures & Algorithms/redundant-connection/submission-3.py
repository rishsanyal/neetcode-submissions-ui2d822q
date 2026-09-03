class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph_so_far = defaultdict(list)

        def path_exists(u, v, seen):
            if u == v:
                return True

            seen.add(u)

            for neighbor in graph_so_far[u]:
                if neighbor not in seen:
                    if path_exists(neighbor, v, seen):
                        return True

            return False


        for (u, v) in edges:
            if path_exists(u, v, set()):
                return [u, v]
            else:
                graph_so_far[u].append(v)
                graph_so_far[v].append(u)

        return []

"""
1, 2
{
    1: [2],
    2: [1]
}

1,3
{
    1: [2,3],
    2: [1]
    3: [1]
}

1,4
{
    1: [2,3,4],
    2: [1]
    3: [1]
    4: [1]
}

3,4
3->1
(1,4,set([3]))
From 1:
(2,4,set([3,1]))
(4,4,set([3,1])) - True
"""