"""

we know the total sum
we know the sum / k

if thats not possible, we increase it
if possible we decrease it

l, r = 0, sum(nums)

mid = (l+r)//2

    if mid possible
        update res
        go smaller
    else:
        go bigger

check function:
    if it's possible to split this subarray into n parts with max sum of input

"""


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        max_sum = 0

        def __check(max_sum):
            curr_sum = 0
            num_subarrays = 0
            num_set = False
            
            res = 0

            for num in nums:
                if ((curr_sum + num) > max_sum) and num_set:
                    num_subarrays += 1
                    curr_sum = num
                else:
                    curr_sum += num

                num_set = True
                res = max(res, curr_sum)

            if ((num_subarrays+1) <= k):
                return res

            return -1

        l, r = 0, sum(nums)

        while l <= r:
            mid = (l+r)//2

            split = __check(mid)

            if split != -1:
                max_sum = max(max_sum, split)
                r = mid - 1
            else:
                l = mid + 1

        return split