class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        cache[0] = 0
        cache[1] = 1

        def r(num):
            if num in cache:
                return cache[num]

            if num <= 0:
                return 0

            cache[num] = r(num-3) + r(num-2) + r(num-1)
            return cache[num]

        return r(n)

