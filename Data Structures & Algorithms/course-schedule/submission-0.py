class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Thoughts:
        - create a graph with requirements and we go down the requirements
        - We have to track which ones are safe to take and which one's aren't
        - if we detect a cycle, we return False

        - create a hashap with key as {a: [b]} - key could be a set
        - we iterate through a random key until we've exhausted all of it's courses and pre-reqs
        - we keep doing that until no dict or the number of courses we can take == numCourses

        # labeled from 0 to numCourses - 1.
        """


        adj_graph = defaultdict(set)
        # safe_courses = set() # For faster lookup

        for (a,b) in prerequisites:
            adj_graph[a].add(b)



        def foo(course, visited):
            if course not in adj_graph:
                return True

            if course in visited:
                return False

            visited.add(course)

            for req in adj_graph[course]:
                if not foo(req, visited):
                    return False

            visited.remove(course)

            return True


        for i in range(numCourses):
            if not foo(i, set()):
                return False

        return True

        

