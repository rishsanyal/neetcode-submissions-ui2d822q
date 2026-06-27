"""
We're implementing the query mechanism

we need to check the smallest window closest to the interval

- find closest intervals, 
- we can have a

- list of heaps
    - we have a list of indices with 1000 elements
    - we go from 0 until intervals where start == query
    - we have a heap of distance
    - pick the shortest


- sort intervals by start time
- soft queries

- go until start == query and collect all of the intersecting intervals in a set
- put them in a heap by distance
- we check the top of the heap for answers and append to result array if possible
Are queries unique? - NO

"""


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        h = []

        queries_info = [(idx, query) for (idx, query) in enumerate(queries)]
        queries_info.sort(key=lambda x: x[1])

        intervals_info = [(idx, interval) for (idx, interval) in enumerate(intervals)]
        intervals_info.sort(key=lambda x: x[1][0])

        res = [-1] * len(queries)

        # We iterate until we see start == query
        for query_idx, query in queries_info:
            while intervals_info and intervals_info[0][1][0] <= query:
                idx, (start_time, end_time) = intervals_info.pop(0)

                heapq.heappush(h, (end_time - start_time + 1, start_time, end_time, idx))
            

            while h and h[0][2] < query:
                heapq.heappop(h)

            if h:
                res[query_idx] = h[0][0]
            else:
                res[query_idx] = (-1)

        return res