class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = sorted(enumerate(tasks), key=lambda x: (x[1][0], x[1][1]))
        h = []
        res = []
        curr_time = 0
        i = 0

        while i < len(tasks) or h:
            while i < len(tasks) and tasks[i][1][0] <= curr_time:
                heapq.heappush(h, (tasks[i][1][1], tasks[i][0]))
                i += 1

            if h:
                end_time, idx = heapq.heappop(h)
                res.append(idx)
                curr_time += end_time
            else:
                # CPU doesn't have a task
                curr_time = tasks[i][1][0]

        return res
