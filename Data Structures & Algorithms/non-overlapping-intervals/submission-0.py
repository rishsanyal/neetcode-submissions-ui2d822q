"""
Do we merge intervals on every index?

THEY'RE NOT SORTED  

Brute force:
- We sort the intervals first
- We remove one interval
- check how many of the remaining ones are overlapping

O(N^N)

We could start tracking groups and check that way?


We could remove one of the overlapping intervals
if it's overlapping already

We sort intervals by end time
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        curr_tracker_end = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            # we check if they overlap
            # if so, we remove the bigger one
            # we update the tracker_end to the smaller one
            # add 1 to res

            curr_start, curr_end = intervals[i]

            if curr_start < curr_tracker_end:
                res += 1
                curr_tracker_end = min(curr_tracker_end, curr_end)
            else:
                curr_tracker_end = curr_end

            # if not, we change the end value
            
        return res