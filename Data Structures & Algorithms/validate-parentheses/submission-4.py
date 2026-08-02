class Solution:
    def isValid(self, s: str) -> bool:
        """
        4 apr 2026
        - output boolean
        
        idea 
        - stack 
            - for every close -> pop out the corresponding open
                - check validity

        - edge invalid cases
            - more open than close
            - more close than open

        11mins
        """

        stack = []
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in close_to_open: # If it is a close now
                if not stack: # no more open -> add this to prevent popping from empty stack
                    return False
                
                top = stack.pop()
                if top != close_to_open[c]:
                    return False
            else: # else is an open
                stack.append(c)
        
        # check against case where open>close -> stack has remaining elements
        return not stack # True is stack is empty











