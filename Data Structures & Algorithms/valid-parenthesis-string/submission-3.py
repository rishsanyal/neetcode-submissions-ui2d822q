"""
We could cache it by number of left parenthesis and right parenthesis
OR number of open brackets

if ( - we start an open backet
if ) - we end an oper bracket
if * - we have to do both?

How do we become greedy with it?

How do I use a stack?
- We use the index and push the index on the three stacks
- we populate the stack but then pick the lowest index and see if we can pop the brackets from there?

"((**)"
"(((*)"

"((**)"

"(*))"


bracket stack - 
star stack    - 2,3

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        bracket_stack, star_stack = deque(), deque()

        for idx, i in enumerate(s):
            if i == "*":
                star_stack.append(idx)
            elif i == "(":
                bracket_stack.append(idx)
            else:
                if bracket_stack:
                    bracket_stack.pop()
                else:
                    if star_stack:
                        star_stack.pop()
                    else:
                        return False

        while bracket_stack and star_stack:
            star_stack_top = star_stack[-1]
            bracket_stack_top = bracket_stack[-1]

            if star_stack_top > bracket_stack_top:
                bracket_stack.pop()
                star_stack.pop()
            else:
                break

        return len(bracket_stack) == 0

        
        