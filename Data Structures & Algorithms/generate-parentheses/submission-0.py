class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def r(curr_str, count):

            if count < 0 or count > n:
                return

            if len(curr_str) == n*2:
                if count == 0:
                    res.append(curr_str)

                return

            r(curr_str + "(", count+1)
            r(curr_str + ")", count-1)

            return

        r("", 0)

        return res