"""
recursive approach

if n == 0: return 1
if n == 1: return x
if n < 1: return (1/x), n
if n > 1: return x*x, n-1

x=2, n=5

2, 5
4, 4
8, 3
16, 2
32, 1
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 1:
            return x
        elif n == 0:
            return 1

        curr_num = 1

        if n > 1:
            curr_num = x
        
        if n < 0:
            curr_num = 1/x
            x = 1/x
            n = -1*n

        while n > 1:
            curr_num *= x
            n -= 1

        return curr_num