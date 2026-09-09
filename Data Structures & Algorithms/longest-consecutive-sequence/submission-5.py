"""
O(N) time
O(N) Space

O(nlgN) time
O(1) space
- So no sorting
- We could put everything in a set
    - cache the longest consecutive until every number
    - hashmap with -1 as value: if -1 then not visited
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Super simple
        # put everything in a set

        nums_set = set(nums)
        tracker = {}

        res = 0

        def __helper(curr_num):
            if curr_num in tracker:
                return tracker[curr_num]

            if curr_num not in nums_set:
                return 0

            tracker_num = curr_num
            curr_res = 0

            while tracker_num in nums_set:
                curr_res += 1
                tracker_num -= 1

            tracker[curr_num] = curr_res
            
            return tracker[curr_num]

        for num in nums:
            res = max(
                res,
                __helper(num)
            )

        return res

