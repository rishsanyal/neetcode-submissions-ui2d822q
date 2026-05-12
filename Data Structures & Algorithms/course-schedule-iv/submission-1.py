class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        We need a flat structure for easy search
        - we can add all pre-reqs as we iterate OR
            we can do a DFS and iterate until we hit the end or the course we're looking for
        
        What if there's a cycle?
        - We need to detect and return False

        We create a directed graph
        - course -> prereq

        We can iterate through numCourses and make it flat and check for cycles
        If no cycles - add to the dict and keep going on
        
        iterate through queries in the end.
        """

        graph = defaultdict(set)
        res = []
        reqs = set()

        prereqMap = {}

        for (prereq, course) in prerequisites:
            graph[course].add(prereq)

        def dfs(course):
            if course not in prereqMap:
                prereqMap[course] = set()
                for req_course in graph.get(course, []):
                    prereqMap[course] |= dfs(req_course)

                prereqMap[course].add(course)

            return prereqMap[course]


        for i in range(numCourses):
            dfs(i)

        # implement search
        for (prereq, course) in queries:
            if not prereq in prereqMap[course]:
                res.append(False)
            else:
                res.append(True)

        return res
            