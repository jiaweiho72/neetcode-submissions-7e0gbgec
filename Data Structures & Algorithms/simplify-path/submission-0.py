class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        26 Aug 2026
        - convert absolute path to simplified canonical path
            - basically clean up to form the barebone orthodox path

        to clean
        '.' cur dir -> just remove '/.'
        '..' prev dir -> move backwards (remove previous dir)
        '///' clean up to be just one /
        '...' ignore

        expected
        start with '/'
        path not end with '/'
        must not have '.'


        idea - stack
        - iterate through path. cur element need to compare with previous and may remove previous elements
        - split by '/' because iterating by character is hard when names are multi character
            - note '///' split into ['', '']
        - stack is all the valid paths

        """

        path_split = path.split('/')
        stack = [] # result

        for directory in path_split:
            if directory == '': # ignore empty
                continue
            elif directory == '.': # cur dir
                continue
            elif directory == '..': # prev dir
                if stack:
                    stack.pop()
            elif directory.startswith('..'): # many ....
                stack.append(directory)
            else: # normal directory
                stack.append(directory)
        
        return '/' + '/'.join(stack) # empty stack returns just '/'















