"""
Count, task

We get the count of each task
populate a max heap with it

if there's only 1 task or the next task is the same, we avoid it


["A","A","A","B","C"]

(3, A),
(1, B),
(1, C)

A,B,C,IDLE,A,IDLE,IDLE,IDLE,A

Count same but alphabets dif?
We can depend on the heap to sort by different alphabets too


["X","X","Y","Y"]

(2, Y),
(2, X)

Y, X, IDLE, Y, X

temp = []

while True:
    if len(res) % k+1 != 0:
        if not h:
            res.append('IDLE')
        else:
            count, task = heapq.heappop_max(h)
            res.append(task)

            if count-1 > 0:
                temp.append([count-1, task])
    elif heap:
        res.append(heapq.heappop_max(h))
    elif len(res) % k+1 == 0:
        while temp:
            heapq.heappush_max(h, temp.pop())


["A","A","A","B","B","B","C","C","C","D","D","E"]
n = 2

[
    [3, A],
    [3, B],
    [3, C],
    [2, D],
    [1, E]
]

ABCABCABCDEID

ABCDEABCDABC


"""


class Solution:

    import heapq

    def leastInterval(self, tasks: List[str], n: int) -> int:

        k = n
        res = []

        c = Counter(tasks)

        h = [[task_count, task] for (task, task_count) in c.items()]

        heapq.heapify_max(h)

        last_task = {}

        temp = []
        last_job = ''

        while True:
            for _ in range(n+1):
                if temp and (len(res) - last_task[temp[0][1]] > k):
                    count, task = temp.pop(0)

                    res.append(task)
                    last_task[task] = len(res)-1

                    if count-1 > 0:
                        heapq.heappush_max(temp, [count-1, task])
                elif h:
                    count, task = heapq.heappop_max(h)
                    res.append(task)

                    last_task[task] = len(res)-1

                    if count-1 > 0:
                        temp.append([count-1, task])
                elif temp:
                    res.append('IDLE')
                else:
                    break
                    
            if not temp and not h:
                break
                            
        # print(res)

        return len(res)

        