"""

[], [1,2,3]
[1], [2,3]
[1,2] [3]
[1,3], [2]
[2], [1,3]



"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def r(curr_list, remaining_list):
            if not remaining_list:
                if len(curr_list) == len(nums):
                    res.append(curr_list[:])
                return

            for (i,idx) in enumerate(remaining_list):
                r(curr_list + [i], remaining_list[:idx-1] + remaining_list[idx+1:])

            r([remaining_list[0]], remaining_list[1:])

        r([], nums)

        return res
