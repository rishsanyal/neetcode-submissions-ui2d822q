"""
we need to check on every level

we take a character / start a string
check if it's a palindrome
if it is, we recurse
else we break
when we have no more characters, we add to res


"aab"

a ab
a,a b
a,a,b "" - Y

a,ab - X

aa b
aa, b - Y

aab - X
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def r(curr_list, remaining_str):
            if not remaining_str:
                res.append(curr_list[:])
                return
            
            new_str = ""
            for idx, new_char in enumerate(remaining_str):
                new_str += new_char

                if new_str != new_str[::-1]:
                    break

                r(curr_list + [new_str], remaining_str[idx+1:])

            return

        r([], s)

        return res