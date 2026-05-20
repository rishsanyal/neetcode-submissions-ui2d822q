"""
At each level we track
curr_sum, 
"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def r(idx, curr_list, total):
            if total == target:
                res.append(curr_list.copy())
                return
                
            if idx >= len(nums):
                return

            if total > target:
                return

                
            curr_list.append(nums[idx])
            r(idx, curr_list, total+nums[idx])
            curr_list.pop()
            r(idx+1, curr_list, total)

            return

        r(0, [], 0)

        return res

            