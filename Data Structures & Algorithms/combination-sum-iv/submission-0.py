"""
We can re-use the current character
OR
We add the next character

We don't go over the target

"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        cache = {}

        def r(curr_sum):
            res = 0
            if curr_sum >= target:
                if curr_sum == target:
                    return 1
                return 0

            if curr_sum in cache:
                return cache[curr_sum]

            for num in nums:
                res += r(curr_sum + num)

            cache[curr_sum] = res

            return cache[curr_sum]

        return r(0)


            
