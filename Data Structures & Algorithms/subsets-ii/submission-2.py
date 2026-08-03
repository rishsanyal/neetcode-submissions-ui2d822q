"""

Normally
sort()

On each level
    index == len(nums):
        append curr_list
        return

    r(curr_list + nums[idx], idx+1)
    while idx < len(nums) and idx == idx+1
        idx += 1
    r([nums[idx]], idx+1)


"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def r(curr_list, curr_idx):
            if curr_idx == len(nums):
                res.append(curr_list[:])
                return
            
            r(curr_list + [nums[curr_idx]], curr_idx+1)

            while curr_idx+1 < len(nums) and nums[curr_idx] == nums[curr_idx+1]:
                curr_idx += 1

            if curr_idx < len(nums):
                r(curr_list, curr_idx+1)

        r([], 0)

        return res

        