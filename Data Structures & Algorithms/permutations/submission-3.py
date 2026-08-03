"""

[], [1,2,3]
[1], [2,3]
[1,2] [3]
[1,3], [2]
[2], [1,3]

We could track visited indices in a set
add to set
add to list
recurse

remove from set


[1], {0}

[1,2]. {0,1}
[1,2,3], {0,1,2}
[1,2], {0,1}
[1,3], {0,2}


"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def r(remaining_list, curr_list):
            if len(curr_list) == len(nums):
                res.append(curr_list[:])
                return

            for i in range(len(remaining_list)):
                r(remaining_list[:i] + remaining_list[i+1:], curr_list + [remaining_list[i]])

        r(nums, [])

        return res
