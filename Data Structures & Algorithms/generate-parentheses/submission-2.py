"""

We can track num_open and the string
0, ""
1, "("

2, "(("
0, "()"



"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def r(num_open, curr_str):
            if len(curr_str) == 2*n:
                if num_open == 0:
                    res.append(''.join(curr_str))
                
                return

            if num_open < 0:
                return

            curr_str.append("(")
            r(num_open + 1, curr_str)
            curr_str.pop()

            curr_str.append(")")
            r(num_open - 1, curr_str)
            curr_str.pop()

        r(0, [])

        return res
