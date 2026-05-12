class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        DFS should still work
        we just need to add it to a global list?

        what's the numCourses for? We can still iterate, 
            we just need to add results in the front of a list

        we also have courses not in list, but those can go anywhere

        make graph
        res = []

        start iterating through numCourses
        if not in graph - add to res

        if in graph: DFS
        if cycle - return False, []
        if true - return temp list and append to res
        """

        graph = defaultdict(set)
        global_visited = set()
        res = []

        # Create graph
        for a,b in prerequisites:
            graph[a].add(b)

        def foo(course, visited):
            nonlocal res

            if course in visited:
                return False

            if course in global_visited:
                return True

            visited.add(course)

            for req in graph.get(course, []):
                status = foo(req, visited)

                if not status:
                    return False

            visited.remove(course)

            if course in graph:
                graph.pop(course)

            res.append(course)
            global_visited.add(course)

            return True


        for i in range(numCourses):
            status = foo(i, set())

            if not status:
                return []


        return res