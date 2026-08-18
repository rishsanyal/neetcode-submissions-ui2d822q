"""
- we have tasks by their enqueue_time and processing_time
- The CPU picks the from all available tasks with shortest processing time
- CPU will process the enitre task then


- We sort tasks by start time (set the curr_time to the first task)
- We put all available tasks in a min heap by a delta processing time, start time, end time
- pick task - update curr_time

[[1,4,0],[2,1,2],[3,3,1]]
curr_time = 1

h = [(4, 0)]
curr_time = 5

h = [(1, 2), (3, 3)]
curr_time = 6

h = [(3, 3)]
curr_time = 9
"""

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tasks = [[task[0],task[1],idx] for (idx, task) in enumerate(tasks)]
        tasks.sort(key=lambda x: x[0])

        h = []
        res = []

        task_idx = 0

        curr_time = tasks[0][0]

        while task_idx < len(tasks) or h:
            while task_idx < len(tasks) and tasks[task_idx][0] <= curr_time:
                _, curr_task_processing_time, curr_task_idx = tasks[task_idx]
                heapq.heappush(h, (curr_task_processing_time, curr_task_idx))

                task_idx += 1

            if h:
                curr_task_proc_time, curr_task_idx = heapq.heappop(h)

                curr_time += curr_task_proc_time
                res.append(curr_task_idx)
            else:
                curr_time = tasks[task_idx][0]

        return res