"""
We pick a number and then we can't pick it again

- sort the list
- loop through the list
- if index in visited, don't continue down that path

"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        visited = set()

        def r(perm):
            if len(perm) == len(nums):
                res.add(tuple(perm))
                return

            for idx in range(len(nums)):
                if idx not in visited:
                    visited.add(idx)
                    r(perm+[nums[idx]])
                    visited.remove(idx)


            return

        r([])

        return list(res)
                    
