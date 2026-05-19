"""
We're given the car's capacity
It's a one way car trip

Feel like this is a graph problem
We have the trips and the capcities, the edges are weighted by people?

We could sort by starting point - make sure we iterate happily
We have a start point and end point, we need to be sure we don't hit anything in between that

Can we pick up more people along the way if there's space?
[[1,1,3],[1,2,4]] - like that? - Yes?

- We put a trip in a heap
    (end_point, capacity, start_point)
- Track total Capacity (subtract cap everytime we enter in heap)
- compare heap on every new entry
- if new start is lt old end, we check capacity and carry on if possible
- if new start is equal to old end, we pop and add

when do we pop from MIN heap

[[3, 2, 7], [8, 3, 9], [3, 7, 9]]
- cap - 3 [(7, 3)]
- cap - 11 [(7, 3), (9, 8)]
- cap - 11 [(9, 3) (9, 8)]
- cap 0 heap 0

"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key=lambda x: (x[1], x[2]))

        print(trips)

        curr_cap, curr_start, curr_end = 0, None, None
        h = []
        
        for (cap, start, end) in trips:
            if not h:
                heapq.heappush(h, (end, cap))
                curr_cap += cap
            else:
                if start < h[0][0]:
                    if cap + curr_cap <= capacity:
                        curr_cap += cap
                        heapq.heappush(h, (end, cap))
                    else:
                        return False
                else:
                    # pop and push
                    _, prev_cap = heapq.heappop(h)
                    curr_cap -= prev_cap

                    curr_cap += cap
                    heapq.heappush(h, (end, cap))

        return True

                