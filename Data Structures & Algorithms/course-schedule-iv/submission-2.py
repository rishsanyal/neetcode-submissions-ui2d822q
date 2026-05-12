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

        for (prereq, course) in prerequisites:
            graph[course].add(prereq)

        prereqMap = {}

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for req_course in graph.get(crs,[]):
                    prereqMap[crs] |= dfs(req_course)

                prereqMap[crs].add(crs)
                
            return prereqMap[crs]
            
        for i in range(numCourses):
            dfs(i)

        # implement search
        for (req, course) in queries:
            if not req in prereqMap[course]:
                res.append(False)
            else:
                res.append(True)

        return res