"""
The number is between smallest of nums and sum(nums)

we do binary search with those bounds
we have a helper function that let's us split nums with a max limit of mid
if we can split it, we go lower
else we go higher

"""


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        num_sum = sum(nums)
        l, r = min(nums), num_sum
        mid = 0
        max_subarray = 0

        def __helper(limit):
            # [1,1,1] -> 2
            # 1
            res = 0
            curr_sum = 0
            max_sum = 0

            for i in nums:
                curr_sum += i

                if curr_sum >= limit:
                    res += 1
                    max_sum = max(max_sum, curr_sum)
                    curr_sum = 0

            result = res + 1 if curr_sum else res
    
            return (result <= k), max_sum



        while l <= r:
            mid = l + (r-l)//2
            split_status, max_subarray = __helper(mid)

            if split_status is True:
                r = mid - 1
            else:
                l = mid + 1

        return max_subarray



        

        

        