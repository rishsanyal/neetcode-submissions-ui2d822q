class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        We need to go by enqueue time because once we hit beyond the curr processing time
            we need to give the CPU a new task to do

        we sort by enqueue time
        we start the first task
        we keep adding to the rest of tasks in a sorted manner (heap) until we're done w 1st task
        pop and continue
        
        [[5,2],[4,4],[4,1],[2,1],[3,3]]
        [(3, 3), (6, 4), (8, 1), (5, 2), (7, 0)] - tasks
        3,4,2,0,1 - ans

        curr_time = 3 - [3]
        curr_time = 6 - [3]

        """

        tasks = [(idx, task[0], task[1]) for idx,task in enumerate(tasks)]
        tasks.sort(key=lambda x: x[1])

        curr_time = None
        h = []
        res = []

        for idx, start_time, end_time in tasks:
            if not curr_time:
                curr_time = start_time + end_time
                res.append(idx)
            elif start_time <= curr_time:
                heapq.heappush(h, (start_time+end_time, idx))
            else:
                # we take a task
                curr_time, new_idx = heapq.heappop(h)
                res.append(new_idx)


                heapq.heappush(h, (start_time+end_time, idx))

        while h:
            _, idx = heapq.heappop(h)
            res.append(idx)

        return res
