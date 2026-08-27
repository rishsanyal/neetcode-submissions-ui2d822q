"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

"""

"""
What's a conflict? 
It's a start time between the previous meeting

- Sort by start time
- validate against previous one
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        if not intervals:
            return True


        curr_start, curr_end = intervals[0].start, intervals[1].end

        for i in range(1, len(intervals)):
            curr_interval = intervals[i]

            if not (curr_start <= curr_interval.start < curr_end):
                return False

            curr_start, curr_end = curr_interval.start, curr_interval.end

        return True
            

            
