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
        tracker = defaultdict(int)

        res = 0

        def __helper(curr_num):
            if curr_num in tracker:
                return tracker[curr_num]

            if curr_num not in nums_set:
                return 0

            tracker[curr_num] = 1 + __helper(curr_num-1)

            return tracker[curr_num]

        for num in nums:
            res = max(
                res,
                __helper(num)
            )

        return res

