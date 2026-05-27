"""
INITIALLY WE PICK A NUMBER between 2 - math.ceil(n/2)

we keep adding it until we hit n
and multiply it in the end

n needs to be divisible by n tho
we go from 1 to (n//2)+1 if it's divisible, we're good


"""

class Solution:
    def integerBreak(self, n: int) -> int:

        cache = {1:1}

        def r(curr_nums, curr_sum):
            max_num = 1
            if curr_sum >= n:
                if curr_sum == n:
                    res = 1
                    for i in curr_nums:
                        res *= i
                    return res

                return 1

            for i in range(1, n):
                max_num = max(max_num, r(curr_nums + [i], curr_sum + i))

            return max_num

        return(r([], 0))
