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
        res = []

        for a,b in prerequisites:
            graph[b].add(a)

        def foo(course, visited, temp_res):
            nonlocal res

            if course in visited:
                return False

            if course not in graph:
                return True

            visited.add(course)

            for req in graph[course]:
                small_res = []
                status = foo(req, visited, small_res)

                if not status:
                    return False

                res += small_res

            visited.remove(course)
            graph.pop(course)

            return True


        for i in range(numCourses):
            course_res = [i]
            status = foo(i, set(), course_res)

            if not status:
                return []

            res = res + course_res


        return res