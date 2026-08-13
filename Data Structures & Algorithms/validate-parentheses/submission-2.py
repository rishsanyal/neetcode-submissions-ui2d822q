class Solution:
    def isValid(self, s: str) -> bool:
        tracker = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for bracket in s:
            if bracket not in tracker:
                stack.append(bracket)
            else:
                if not stack:
                    return False

                prev_bracket = stack.pop()

                if prev_bracket != tracker[bracket]:
                    return False

        return stack == []