"""
We could add the interval
sort the array
merge intervals as we go on?


we could insert interval according to start time
iterate forward and merge intervals 2 at a time

[[1,3],[4,6]]
[[1,2],[3,5],[4,6]]

[[1,2],[3,6]]

optimization - O(1) space

we iterate through the list
for every element
if it can be merged, it's merged and added to res
if it can't be merged with the new interval, it's added to res



"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for idx in range(len(intervals)):
            curr_start, curr_end = intervals[idx]

            if not res:
                res.append([curr_start, curr_end])
            else:
                prev_start, prev_end = res[-1]

                # check if newInterval and it can be merge

                if newInterval and ((curr_start <= newInterval[0] <= curr_end) or ((curr_start <= newInterval[1] <= curr_end))):
                    curr_start, curr_end = min(curr_start, newInterval[0]), max(curr_end, newInterval[1])
                    newInterval = None

                if ((prev_start <= curr_start <= prev_end) or (prev_start <= curr_end <= prev_end)):
                    res[-1] = min(curr_start, prev_start), max(curr_end, prev_end)
                else:
                    res.append((curr_start, curr_end))

        if newInterval:
            res.append(newInterval)
            res.sort(key=lambda x: x[0])
                
        return res