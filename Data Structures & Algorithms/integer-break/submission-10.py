class Solution:
    def integerBreak(self, n: int) -> int:
        
        cache = {1:1}
        ans = 1

        def r(num):
            if num in cache:
                return cache[num]

            cache[num] = num if num != n else 1

            for i in range(1, num):
                cache[num] = max(cache[num], r(i)*r(num-i))

            return cache[num]

        return r(n)

                