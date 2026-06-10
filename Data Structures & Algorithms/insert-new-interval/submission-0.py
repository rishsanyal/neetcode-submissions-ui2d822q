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

"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for (idx, (start, end)) in enumerate(intervals):
            if end > newInterval[1]:
                intervals.insert(idx, newInterval)
                newInterval = None
                break

        if newInterval:
            intervals.append(newInterval)

        print(intervals)

        for idx in range(len(intervals)):
            curr_start, curr_end = intervals[idx]

            if not res:
                res.append([curr_start, curr_end])
            else:
                prev_start, prev_end = res[-1]

                if (prev_start <= curr_start <= prev_end) or (prev_start <= curr_end <= prev_end):
                    res[-1] = [min(prev_start, curr_start), max(curr_end, prev_end)]
                else:
                    res.append([curr_start, curr_end])

        return res