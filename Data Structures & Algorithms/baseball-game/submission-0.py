class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Like polish notation
        - stack: when you push elements and only when you meet an operator, you pop the stack top operands

        operationsa are always valid

        - don't pop in this case
        """

        n = len(operations)
        stack = []

        for i in range(n):
            operation = operations[i]
            if operation == "+":
                right = stack[-1]
                left = stack[-2]
                stack.append(left + right)

            elif operation == "D":
                stack_top = stack[-1]
                stack.append(stack_top * 2)

            elif operation == "C":
                stack_top = stack.pop()

            else: # it is an integer
                stack.append(int(operation))
        return sum(stack)

