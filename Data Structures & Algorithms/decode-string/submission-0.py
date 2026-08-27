class Solution:
    def decodeString(self, s: str) -> str:
        """
        27 Aug 2026
        - Inputs are well-formed
        - For each k[s]
        - like Math multiplication, bracket order matters

        Stack
        - iterate for each character
        - if on every close ']' pop and process the inner string
            - as string is many characters, hard to track exactly where the current string starts from
        solution
        - split by ']' closed
        - for each element (except for 1st) pop the 
        does not work if ]]. You need to process the ] on the fly instead of processing all at once in first pass
        input guarateed valid 


        you can just pop while it is alpha

        - Key: meet a ']' closed bracket, it is the correct time to process immediately (ligma)
            for ]] you would alr process the first ] so it is still correct
        - decoded put back in the stack for later processing
        mistake: stack pops like this
        [1,2] -> 2 then 1
        so if you append test += stack.pop(), it becomes 21 instead of 12
        so must do test = stack.pop() + test to reverse
        """


        n = len(s)
        stack = [] # list and then join -> save space

        for i in range(n):
            c = s[i]
            if c == ']':
                '''
                processs the previous
                int[ccccccc]
                '''
                string = ''
                while stack and stack[-1].isalpha(): # pop until no alphabets. note: checking stack not needed as question gurantees valid form
                    string = stack.pop() + string
                
                # stack[-1] stops at non alphabet -> '[' open bracket
                stack.pop() # pop '['

                digit = ''
                while stack and stack[-1].isdigit(): # check stack as if first element the next would be out of bounds <0
                    digit = stack.pop() + digit
                digit = int(digit)

                for j in range(digit):
                    stack.append(string)

            else:
                stack.append(c)

        return ''.join(stack)










        