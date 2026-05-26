"""
At every stage, we have to subtract the biggest square number down to 1
int(math.sqrt(13)) = 3.6 ~ 3,2,1
and keep going on that until we hit target

We need to go in reverse order because we want the least amount of numbers
"""

class Solution:
    def numSquares(self, n: int) -> int:

        max_num = int(math.sqrt(n))
        cache = defaultdict(lambda: n+1)

        def r(curr_num_count, curr_sum=0):
            if curr_sum > n:
                return n + 1

            if curr_sum == n:
                return curr_num_count

            if curr_sum in cache:
                return cache[curr_sum]

            for i in range(max_num, 0, -1):
                cache[curr_sum] = min(cache[curr_sum], r(curr_num_count+1, curr_sum+(i**2)))

            return cache[curr_sum]


        return r(0, 0)