class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)

        seen = set()

        for truster,trustee in trust:
            graph[trustee].append(truster)
            seen.add(truster)

        print(graph)

        for trustee, trusters in graph.items():
            if len(trusters) == n-1 and trustee not in seen:
                return trustee

        return -1