"""
On each level, we either add an element and we don't


"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def r(curr_list, idx):
            if idx == len(nums):
                res.append(curr_list[:])
                return
            
            r(curr_list + [nums[idx]], idx+1)
            r(curr_list, idx+1)

        r([], 0)

        return res
        