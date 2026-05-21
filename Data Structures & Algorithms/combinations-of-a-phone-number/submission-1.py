"""
- we need to create a mapping here
- for every character of the map, when there's no more characters left, we add to global list.

How is this backtracking? We could pop it off a list if we need to
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:        
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        res = []

        def r(curr_str, res_str):
            if not curr_str:
                res.append(res_str)
                return

            curr_char = curr_str[0]
            next_chars = list(digitToChar[curr_char])

            for char in next_chars:
                r(curr_str[1:], res_str + char)

            return
        
        r(digits, '')

        return res








        