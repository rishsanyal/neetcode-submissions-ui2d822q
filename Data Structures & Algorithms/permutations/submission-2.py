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

        def r(curr_list, visited):
            if len(visited) == len(nums):
                res.append(curr_list)
                return

            for (idx, val) in enumerate(nums):
                if idx in visited:
                    continue

                visited.add(idx)
                r(curr_list+[val], visited)
                visited.remove(idx)


        r([], set())

        return res
