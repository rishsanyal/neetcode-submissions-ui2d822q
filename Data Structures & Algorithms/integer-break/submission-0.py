"""
INITIALLY WE PICK A NUMBER between 2 - math.ceil(n/2)

we keep adding it until we hit n
and multiply it in the end

n needs to be divisible by n tho
we go from 1 to (n//2)+1 if it's divisible, we're good


"""

class Solution:
    def integerBreak(self, n: int) -> int:


        # def r(curr_num, curr_sum):
        #     if curr_sum >= n:
        #         if curr_sum == n:
        #             return n**(n/curr_num)

        #         return 1

        #     r(curr_num, curr_sum + curr_num)

        res = 0

        for i in range(1, (n//2)+1):
            if (n % i) == 0:
                num = n/i
                res = max(res, i**num)


        return int(res)