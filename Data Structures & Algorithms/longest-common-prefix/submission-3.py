class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        1 Aug 2026
        - return longest common prefix of all strings
            - if none, return ""

        idea
        - search col by col
            - check all str for current col
        
        note: you can just choose any str length to iterate as
            - you just need to be >= min length which is basically every length
        """

        no_of_strs = len(strs)
        random_str_length = len(strs[0])

        # iterate col by col
        for col in range(random_str_length): 
            # iterate row by row (str by )
            base_char = strs[0][col]
            for row in range(no_of_strs):
                cur_str = strs[row]
                # check if col still in current string range
                # check if char are the same
                if col > len(cur_str) - 1 or cur_str[col] != base_char:
                    return cur_str[:col]

        # reach here, means case where all strings are same
        return strs[0] # return any string




        