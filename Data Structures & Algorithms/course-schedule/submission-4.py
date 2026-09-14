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

        def dfs(curr_course, visited):
            if curr_course in visited:
                return -1

            if curr_course in cache:
                return cache[curr_course]

            if curr_course not in graph:
                return 1

            visited.add(curr_course)
            res = 0

            for dependecy in graph[curr_course]:
                temp = dfs(dependecy, visited)

                if temp == -1:
                    res = -1
                    break
                
                res += temp

            cache[curr_course] = res
            return res

        ans = 0
        for i in range(numCourses):
            ans = max(ans, dfs(i, set()))
        
        return ans == numCourses-1