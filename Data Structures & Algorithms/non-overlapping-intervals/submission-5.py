"""
Return minimum number of intervals to remove to make rest of intervals non-overlapping
sort by end time
we need the intersection count of each 
remove the ones with the biggest intersection count (we need to remove the ones that span the longest)

[[1,2],[3,7],[2,8],[5,8]]


"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0

        intervals.sort(key=lambda x: x[1])

        curr_end_time = -100000

        for interval in intervals:
            intersecting = (interval[0] < curr_end_time <= interval[1])

            if intersecting:
                res += 1
            else:
                curr_end_time = interval[1]

        return res

