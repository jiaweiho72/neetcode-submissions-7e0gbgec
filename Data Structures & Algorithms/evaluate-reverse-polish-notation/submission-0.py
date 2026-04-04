class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        4 apr 2026
        notes
        - return the evaluation
        - division truncates to zero -> int(/)

        idea: reverse polish notation
        - from left to right
        - numbers push to a stack
        - if meet an operator, pop out last two numbers and evaluate
        - then push result back to stack

        * note the order or pop is opposite to the order you want
        """

        stack: List[int] = []
        for token in tokens:
            if token == '+':
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
                
            elif token == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)

            elif token == '*':
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)

            elif token == '/':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))

            else:
                stack.append(int(token))

        return stack[0]

