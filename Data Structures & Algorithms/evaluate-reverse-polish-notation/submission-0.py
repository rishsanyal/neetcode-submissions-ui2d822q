class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(num1, num2):
            return num1 + num2

        def multiply(num1, num2):
            return num1 * num2

        def subtract(num1, num2):
            return num1 - num2

        def divide(num1, num2):
            return num1/num2

        operations = {
            "*": multiply,
            "+": add,
            "-": subtract,
            "/": divide
        }

        stack = []

        for token in tokens:
            if token in operations:
                num1, num2 = stack.pop(), stack.pop()
                stack.append(operations[token](num1, num2))
            else:
                stack.append(int(token))

        return stack[-1]
