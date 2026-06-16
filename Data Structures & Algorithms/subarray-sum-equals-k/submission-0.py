"""


- we sort the array
- we add a number to the array


Brute Force:
i in range(len(nums)):
    sum = 0
    j in range(i: len(nums))


We create a dict as we go along
we track the sum and the count of sumarrays with that sum in that map. 
once we reach a sum, we subtract that from target and check if we have the difference in the map
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tracker = {0:1}
        curr_sum = 0
        res = 0

        for n in nums:
            curr_sum += n
            res += tracker.get(curr_sum-k, 0)
            tracker[curr_sum] = tracker.get(curr_sum, 0) + 1

        return res

