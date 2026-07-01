"""
We have to check the first few characters of str2, get it's common divisor 
and the same then for str1

we create a helper that yields the string divisor - helper
we need a checking function too

we give it a string
from len(1, len(input)): it create sa new divisor and checks the entire string

----------

We could sum the integers of all of str1
sum the integers of all of str2

keep dividing the by 0, the length

str2[0:ans] is the length?

A = 1
B = 2

1+2+1+2 = 6

1+2 = 3



"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def __return_sum(inp_str):
            res = 0
            for i in inp_str:
                res += int(ord('A') + ord(i))

            return res



        # We assume str1's always greater
        if len(str2) > len(str1):
            str2, str1 = str1, str2

        print(__return_sum(str2))

        return ''

        


        