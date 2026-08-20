"""

global res

- i from n -> 0
 if n%i == 0:
    res = max(res, (i)**(n/i))

"""

class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 0
        cache = {}

        def r(num):
            nonlocal ans
            res = 1

            if num in cache:
                return cache[num]
            
            if num == 1:
                return 1

            cache[num] = 1 if num == n else num

            for i in range(1, num):
                res = r(i) * r(num-i)
                cache[num] = max(res, cache[num])

            return cache[num]

        return r(n)