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
        l, r = max(nums), num_sum
        mid = 0
        max_subarray = 0

        res = float('inf')

        def __helper(mid_lim):

            temp = []
            curr = 0
            curr_greatest = -1

            for i in nums:
                if curr + i > mid_lim:
                    temp.append(curr)
                    curr_greatest = max(curr_greatest, curr)
                    curr = i
                elif curr + i < mid_lim:
                    curr += i
                else:
                    temp.append(curr+i)
                    curr_greatest = max(curr_greatest, curr + i)
                    curr = 0

            if curr != 0:
                temp.append(curr)

            if curr_greatest > res:
                return False
            
            if len(temp) > k:
                return False

            return True

        final_result = num_sum

        while l <= r:
            mid = (r+l)//2
            split_status = __helper(mid)

            if split_status:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res

