class MinStack:
    """
    6 apr 2026
    notes
    - each must be O(1)
        - push append to back
        - pop backside
        - get element
        - get min
            - additional space data structure to keep track of the min at every iteration
                - make sure it is synced with the level of iteration with main stack

    - will always be called on non-empty stacks so no need to check
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(self.min_stack[-1] if self.min_stack else val, val)) # handle first element min_stack is empty
        # return None # not needed

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        
