"""
We have a limit attached with each index

we want max(r(0, len(nums)-2), r(1, len(nums)-1)

def r(l, r):
    if l >= r:
        return 0

    if l in cache:
        return cache[l]

    cache[l] = nums[l] + r(l+2, r)

    return cache[l]

    

    
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(l, r):
            if l >= r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            cache[(l, r)] = max(nums[l] + dfs(l+2, r), dfs(l+1, r))

            return cache[(l, r)]

        return max(dfs(0, len(nums)-1), dfs(1, len(nums)))

        