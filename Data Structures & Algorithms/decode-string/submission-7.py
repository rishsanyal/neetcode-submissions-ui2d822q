"""

we have to track curr number and curr string
this happens in a stack

"2[a3[b]]4[c]"
curr_str = abbb*2

abbbabbb + cccc
stack = [
]

if not stack - add to res str

We can just add to the stack directly

we append to stack on [

- append to stack
- pop from stack - make result string - append to antoher stack

for every new number
we start tracking the new number and the new string until ]
when we see a ]
we stop tracking
multiply by curr num
append to stack
"""


class Solution:
    def decodeString(self, s: str) -> str:

        counts, chars = [], []
        curr_str, curr_num = '', ''

        for fuckMe in s:
            if fuckMe.isalpha():
                curr_str += fuckMe
            elif fuckMe.isnumeric():
                curr_num += fuckMe
            elif fuckMe == ']':
                temp = curr_str

                curr_count = counts.pop()
                curr_str = chars.pop()

                curr_str = curr_str + (temp * int(curr_count))

                curr_count = ''
            else:
                chars.append(curr_str)
                counts.append(curr_num)

                curr_str = ''
                curr_num = ''
        return curr_str

                






        