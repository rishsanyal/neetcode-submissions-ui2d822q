"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
We'll have to sort the intervals by the start time
iterate through them to check for clashes

[,(5,10),(15,20)]
(0, 30)
(5, 10)


"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)

        prev_start, prev_end = intervals[0].start, intervals[0].end

        for interval in intervals[1:]:
            curr_start, curr_end = interval.start, interval.end

            if (prev_start <= curr_start < prev_end) or (prev_start < curr_end <= prev_end):
                return False

            prev_start, prev_end = curr_start, curr_end

        return True
