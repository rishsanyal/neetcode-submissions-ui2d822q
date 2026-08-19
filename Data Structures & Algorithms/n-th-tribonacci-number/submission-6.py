class Solution:
    def tribonacci(self, n: int) -> int:
        
        cache = {0:0, 1:1, 2:1}


        def h(num):
            if num in cache:
                return cache[num]

            # if num <= 0:
            #     return 0

            cache[num] = h(num-1) + h(num-2) + h(num-3)

            return cache[num]

        return h(n)