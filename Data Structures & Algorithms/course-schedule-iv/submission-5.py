"""
- We need a flat directory structure for prerequisites
- We can do a lookup easily in that way


[prereq, course]

- For each course N
    -   We have all prerequisties for it  
    -   we have a local set per recursion
    -   recurse on prereq - get result of all of it's prereq
        -   add the result to a set then
    
    return
    


[[1,0],[2,1],[3,2]]
{
    0: [1],
    1: [2],
    2: [3],
    3: []
}




- Assuming valid data/no cycles
- What if 2 courses have the same preqreq? - We'll deal with it

"""




class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        course_reqs = defaultdict(set)

        for prereq, course in prerequisites:
            course_reqs[course].add(prereq)

        tracker = defaultdict(set)

        def __helper(curr_course):
            if curr_course in tracker:
                return tracker[curr_course]
                
            res = set()

            for prereq in course_reqs[curr_course]:
                res.add(prereq)
                res |= __helper(prereq)

            tracker[curr_course] = res

            return res


        for i in range(numCourses):
            if i not in tracker:
                __helper(i)

        res = []

        for a,b in queries:
            res.append(a in tracker[b])

        return res

        