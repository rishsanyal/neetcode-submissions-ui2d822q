"""
On each level, we choose current number again or we move to a new number
we can pick the same number again, as long as the curr sum <= target
else we we don't

we move to a new number
[new_num] [prev_sum + new_num] [prev_sum += same number?]

keep adding same num until we hit sum


if sum <= target:
    We add same index
    we recurse
    we pop last number

    we add new number
    we recurse

if sum == target:
    add to list
    return
if sum > target:
    return
    


"""


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        
        def r(curr_idx, curr_sum, curr_list):
            if curr_sum == target:
                print(curr_sum)
                res.append(curr_list[:])
                return

            
            if curr_idx == len(nums):
                return


            if curr_sum < target:
                # We add same index
                # we recurse
                # we pop last number

                # we add new number
                # we recurse
                r(curr_idx, curr_sum + nums[curr_idx], curr_list + [nums[curr_idx]])
                r(curr_idx+1, curr_sum, curr_list)

            return

        r(0, 0, [])

        return res