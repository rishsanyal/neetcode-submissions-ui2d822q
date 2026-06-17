"""
Stack of stacks?
we have an int

Every time we see a new number, we start a stack?

abbbabbbc

every time we see
- bracket close, we pop from stack
- brack open, we add to stack
- if we pop from stack and the previous element is a str, we add to it

abbbabbb c

return .join


axb3[z]4[c]

axb, 3, z, 4, c

How about we use 2 stacks? Count Stack and string stack

curr_str, curr_char

Everytime we see a bracket open, we add to the stack
in the end we also reset and add to the stack
every time we see it close, we pop from both and add to the string stack
"""


class Solution:
    def decodeString(self, s: str) -> str:
        curr_str, curr_count = '', ''
        str_stack, count_stack = [], []
        new = True


        for c in s:
            if c == '[':
                str_stack.append(curr_str)
                count_stack.append(curr_count)

                curr_count = ''
                curr_str = ''
            elif c == ']':
                temp = curr_str

                curr_count = count_stack.pop()
                curr_str = str_stack.pop()

                curr_str += temp * int(curr_count)

                curr_count = ''
            elif c.isdigit():
                curr_count += c
            else:
                curr_str += c

        return curr_str


                











        