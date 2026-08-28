"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
- sort meetings by start time
- We check for a conflict
    conflict: start time between the previous meeting's time


- sort by end time?
[(0,40),(5,10),(15,20)]

[(5, 10), (15, 24), (16, 30), (25, 40)]
we could track the conflict and use the smaller time for the conference rooms?


[(5, 10), (15, 24), (16, 30), (25, 40)]

"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        h = []

        for interval in intervals:
            while h and h[0] <= interval.start:
                heapq.heappop(h)

            heapq.heappush(h, interval.end)

        return len(h)