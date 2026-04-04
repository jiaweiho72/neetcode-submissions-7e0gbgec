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

        """

        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack: # no more open
                    return False
                if c == ")":
                    top = stack.pop()
                    if top != "(":
                        return False
                elif c == "}":
                    top = stack.pop()
                    if top != "{":
                        return False
                elif c == "]":
                    top = stack.pop()
                    if top != "[":
                        return False
                else:
                    return False
        
        # check against case where open>close -> stack has remaining elements
        return not stack # True is stack is empty











