"""
We could use ord to map the characters

At each level, we either group a character or we treat it as individual
- we can only group it if the grouping is less than 26
- if it's 0 we have to group it too. Could be invalid if 0 is leading

index, len of numbers?

12
- 0, [1] --- 0, 1
- [12], [1,2] --- 1,1 and 1,2


01
- [0] --- 0, 1
- [01], [0, 1] --- 

we could also start appending characters directly?

index, last_number
12
- 0, [a], 1 --- 0, 1
- 1, [ab], 2 and [l], 12


226 - 0, , []
26 - 1, ,[b] and 1, 2, [], b
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        num_dict = {str(i - 97 + 1):chr(i) for i in range(97, 97+26)}

        cache = {}

        def r(idx):
            res = 0

            if idx == len(s):
                return 1

            if idx in cache:
                return cache[idx]

            one_char = s[idx: idx+1]
            two_char = s[idx: idx+2]

            if one_char in num_dict:
                res += r(idx+1)
            
            if two_char in num_dict:
                res += r(idx+2)

            cache[idx] = res

            return cache[idx]
            

        return r(0)