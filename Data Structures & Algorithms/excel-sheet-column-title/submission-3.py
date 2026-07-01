"""
We're given an int
We need to convert that into an excel row title

there's 26 numbers in the alphabet
After that we add an A in front

We can keep // by 26 and append numbers as we go on

We can make this recursive

AA - 27 - 26 + 1

BA - 53 -> (26*2)


800 - char(799 % 26) + r(799 // 26)
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        if columnNumber <= 0:
            return ''

        n = columnNumber - 1

        curr_char_repr = n // 26
        return self.convertToTitle(curr_char_repr) + chr(n % 26 + ord('A'))