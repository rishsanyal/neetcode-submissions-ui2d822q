"""
We're given an int
We need to convert that into an excel row title

there's 26 numbers in the alphabet
After that we add an A in front

We can keep // by 26 and append numbers as we go on

We can make this recursive

AA - 27 - 26 + 1

BA - 53 -> (26*2)
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        if columnNumber <= 0:
            return ''
        
        if columnNumber <= 26:
            return chr(64 + columnNumber)

        curr_char_repr = columnNumber // 26
        curr_char_remainder = columnNumber - (26 * curr_char_repr)

        res = chr(64 + curr_char_repr) + self.convertToTitle(curr_char_remainder)

        return res