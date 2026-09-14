"""

- We need a dependecy graph
- we need to track visited classes and the longst path they can take
- if at any point, the answer = n-1, we return

- there should be no cycles - if cycle, set the answer to -1
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cache = {}
        graph = defaultdict(set)

        state = False

        if not prerequisites:
            return True

        for a,b in prerequisites:
            graph[a].add(b)

            if a == b:
                return False

        def dfs(curr_course, visited):
            if curr_course in visited:
                return False

            # if curr_course in cache:
            #     return cache[curr_course]

            if curr_course not in graph:
                return True

            visited.add(curr_course)

            for dependecy in graph[curr_course]:
                if not dfs(dependecy, visited):
                    return False

            visited.remove(curr_course)

            # cache[curr_course] = True
            return True

        ans = 0
        for i in range(numCourses):
            ans = max(ans, dfs(i, set()))

            if not ans:
                return False

        return True