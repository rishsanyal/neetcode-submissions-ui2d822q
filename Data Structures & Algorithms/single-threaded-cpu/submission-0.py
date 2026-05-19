class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        Sort by enqueue time
        We have to wait until enqueueTime + prev_processing time

        we have to populate this in a heap because we need the duration and the index

        while we're under that time, we can gather everything we need to in a heap 
        and keep getting operations done

        curr_task_time = None
        """

        tasks = [(idx, task[0], task[1]) for idx,task in enumerate(tasks)]

        # sorted by enqueue time
        tasks.sort(key=lambda x: x[1])
        n = len(tasks)

        print(tasks)

        start_time = None
        curr_end = None
        
        curr_task_time = None

        temp_heap = []
        res = []

        for (task_idx, enqueue_time, processing_time) in tasks:
            if not curr_task_time:
                curr_task_time = enqueue_time

            if curr_task_time >= enqueue_time:
                heapq.heappush(temp_heap, (processing_time, task_idx, enqueue_time))
            else:
                # we pop all
                # we add new job to heap if possible

                while temp_heap:
                    enq, idx, proc = heapq.heappop(temp_heap)
                    curr_task_time = enq + proc

                    res.append(idx)

                if curr_task_time >= enqueue_time:
                    heapq.heappush(temp_heap, (enqueue_time, task_idx, processing_time))

            
        while temp_heap:
            _, idx, _ = heapq.heappop(temp_heap)
            res.append(idx)

        return res