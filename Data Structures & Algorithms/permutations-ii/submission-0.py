"""
We pick a number and then we can't pick it again

Approach
- we sort the nums list
- we loop through the input list
- we pick a number
- we pass the rest of the list to the recursive function
- we stop when there's no more list

[1,1,2]
[1], [1,2]
[1,1] [2]
[1,1,2]
[1,2] [1]
[1,2,1]
[2] [1,1]
[2,1] [1]
[2,1,1]
[2] [1,1]
[2,1,1]

We could make it unique by making it a tuple

We could ONLY pick new numbers
[1,1,2]
[1], [1,2]
[1,1] [2]
[1,1,2]
[1,2] [1] - ?
[2], [1,1]
[2,1,1]


"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        visited_set = set()

        def r(inp_list):
            if len(inp_list) == len(nums):
                res.add(tuple(inp_list))
                return

            for idx, element in enumerate(nums):
                if idx not in visited_set:
                    visited_set.add(idx)
                    r([element]+inp_list)
                    visited_set.remove(idx)

        r([])
        return list(res)

