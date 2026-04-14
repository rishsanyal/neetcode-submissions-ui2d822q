class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for char in s:
            if char in bracket_map and stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                stack.append(char)

        return stack == []