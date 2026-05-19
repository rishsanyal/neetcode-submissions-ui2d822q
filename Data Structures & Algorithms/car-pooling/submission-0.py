"""
We're given the car's capacity
It's a one way car trip

Feel like this is a graph problem
We have the trips and the capcities, the edges are weighted by people?

We could sort by starting point - make sure we iterate happily
We have a start point and end point, we need to be sure we don't hit anything in between that

Can we pick up more people along the way if there's space?
[[1,1,3],[1,2,4]] - like that? - Yes?

"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key=lambda x: (x[1], x[2]))

        curr_cap, curr_start, curr_end = None, None, None

        while trips:
            # No previous trip
            if not curr_start:
                curr_cap, curr_start, curr_end = trips.pop(0)
            else:
                # new trip
                new_cap, new_start, new_end = trips.pop(0)

                # check if compatible
                if not (new_start >= curr_end):
                    return False

                curr_cap = new_cap
                curr_start, curr_end = new_start, new_end

        return True

                








