"""
We have to track the min number of jumps to get the every index
check which index gets us to the last place first

on every level we track the number of hops
if we update the distance, we increase the hops? - fishy
on every hop, we have to track the max distance we can go

[2,3,4,0,0,1]
[0,1,1,2,2,2] - 2
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        tracker = [101] * len(nums)
        tracker[0] = 0

        for idx, num in enumerate(nums):
            curr_jumps = tracker[idx]

            for j in range(idx+1, min(idx+num+1, len(nums))):
                tracker[j] = min(tracker[j], curr_jumps+1)

        return tracker[-1]