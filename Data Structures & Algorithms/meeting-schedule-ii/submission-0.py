"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Every time there's a conflict, we provide a different room
We can track the meetings in the different rooms with a dict?

We track the room's usage with the meeting's end time

If there's a conflict, we have to check all previous rooms and see if there's a conflict with all of them?

we could track a min of which room frees up the earliest? - We would've used a heap for this if it weren't an issue

if there's an overlap, we put the sooner ending meeting at the beginning of the room list?
we iterate through the room list to check if any room's available


we get the sorted start times and end times

if start time < curr_end_time -> room += 1, start_time_ptr += 1
if start_time > curr_end_time -> end_time_pointer += 1
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start_times = []
        end_times = []

        for i in intervals:
            (start, end) = i.start, i.end
            start_times.append(start)
            end_times.append(end)

        start_times.sort()
        end_times.sort()

        rooms = 0

        start_time_idx = 0
        end_time_idx = 0

        while start_time_idx < len(start_times) and end_time_idx < len(end_times):
            curr_start_time, curr_end_time = start_times[start_time_idx], end_times[end_time_idx]

            if curr_start_time < curr_end_time:
                rooms += 1
                start_time_idx += 1
            else:
                end_time_idx += 1
                rooms -= 1

        return rooms











