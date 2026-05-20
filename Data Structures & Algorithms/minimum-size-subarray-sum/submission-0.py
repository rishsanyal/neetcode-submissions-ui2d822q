"""
we have two pointers l and r
we keep a counter
as we go on we keep adding the r value to the counter
if the ctr value goes over target, we increase l and remove that from the ctr

for eahc iteration, we track the length
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        curr_sum = 0
        res = float('inf')

        while end < len(nums):
            curr_sum += nums[end]

            while curr_sum >= target:
                res = min(res, end-start+1)
                curr_sum -= nums[start]
                start += 1


            end += 1

        return res if res != float('inf') else 0