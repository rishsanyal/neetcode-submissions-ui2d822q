"""
INITIALLY WE PICK A NUMBER between 2 - math.ceil(n/2)

we keep adding it until we hit n
and multiply it in the end

n needs to be divisible by n tho
we go from 1 to (n//2)+1 if it's divisible, we're good


"""

class Solution:
    def integerBreak(self, n: int) -> int:

        cache = {}

        def r(curr_nums, curr_sum):
            max_num = 1
            
            if curr_sum >= n:
                if curr_sum == n:
                    res = 1
                    for i in curr_nums:
                        res *= i
                    cache[(len(curr_nums), curr_sum)] = max(res, cache.get((len(curr_nums), curr_sum), 0))
                    return cache[(len(curr_nums), curr_sum)]

                return 1

            if curr_sum in cache:
                return cache[(len(curr_nums), curr_sum)]

            for i in range(1, n//2+1):
                max_num = max(max_num, r(curr_nums + [i], curr_sum + i))

            cache[(len(curr_nums), curr_sum)] = max(max_num, cache.get((len(curr_nums), curr_sum), 0))

            return max_num

        return(r([], 0))
