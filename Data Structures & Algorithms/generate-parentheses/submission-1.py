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
                    res.append(curr_str)
                
                return

            if num_open < 0:
                return

            r(num_open + 1, curr_str+"(")
            r(num_open - 1, curr_str+")")

        r(0, "")

        return res

