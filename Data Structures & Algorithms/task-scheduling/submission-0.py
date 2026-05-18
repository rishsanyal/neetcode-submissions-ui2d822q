class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        We count the tasks
        We put all of them in a heap
        We pop it N times, if the heap is empty we increate the counter and go on

        ["A","A","A","B","C"], n = 3
        [3A, B1, C1]
        ABCXAXXXA
        n+1 tasks need to be done per "round"

        tasks = ["X","X","Y","Y"], n = 2
        [2X, 2Y]

        XY

        Track the previous N in a dict
        """
        # import heapq

        ctr = 0
        h = []
        no_task = 0

        c = Counter(tasks)

        for char, count in c.items():
            heapq.heappush_max(h, (count, char))

        while h:
            temp_h = []
            for _ in range(n+1):
                ctr += 1

                if not h:
                    print("No task")
                    no_task += 1
                    continue

                no_task = 0
                count, char = heapq.heappop_max(h)

                print(char)

                if count - 1:
                    temp_h.append((count-1, char))

            while temp_h:
                heapq.heappush_max(h, temp_h.pop())

        return ctr if no_task == 0 else ctr - no_task
