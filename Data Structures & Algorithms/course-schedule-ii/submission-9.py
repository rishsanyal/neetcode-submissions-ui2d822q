"""

Return a valid order of courses you can take

We have the course and it's pre-requisties

BFS or DFS?
Is valid ordering a search problem? DFS should work too

Detecting Cycles?
We detect one, we're done because that makes the order invalid

- Create a dependency dict
- iterate through all dependencies
    - get the order for current dependency
    - get the order for that course
    - get the order for the next course

- What is the difference between a cycle and taking a class previously


[[0,1],[1,0]]

- 0
[0]

(1, {}, {0})



IDEAL CASE

seen = set()

for i in range(n):
    res += __helper(i, seen)
    seen.add(i)

__helper(i, seen=set(), cycle=set()):
    order = [i]

    course_dependecies = dependencies.get(i, [])
    for dep in course_dependecies:
        if dep in seen:
            continue
        if dep in cycle:
            raise Exception

        order += __helper(dep, seen, cycle | set([i]))

    return order




"""



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        seen = set()
        res = []
        global_visited = set()

        dependencies = defaultdict(list)

        for course, prereq in prerequisites:
            dependencies[course].append(prereq)

        def __helper(course, seen=set()):
            nonlocal res

            if course in seen:
                return False

            if course in global_visited:
                return True

            seen.add(course)

            for req in dependencies.get(course, []):
                status = __helper(req, seen)

                if not status:
                    return False

            seen.remove(course)

            global_visited.add(course)
            res.append(course)

            return True

        for i in range(numCourses):
            if i not in res:
                s = __helper(i, seen)

                if not s:
                    return []



        return res