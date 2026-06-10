"""
we could sort and then only go off the last number?

On each level, we either 

[1,1,2]

[1]
[1,1]
[1,1,2]
[1,2]?
[2]
[]

we pick current number
we skip current number until the new index

 

"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def r(idx, curr_nums=[]):
            if idx == len(nums):
                res.append(curr_nums[:])
                return

            r(idx+1, curr_nums + [nums[idx]])

            while idx < len(nums)-1 and nums[idx] == nums[idx+1]:
                idx += 1

            r(idx+1, curr_nums)

            return


        r(0)

        return res