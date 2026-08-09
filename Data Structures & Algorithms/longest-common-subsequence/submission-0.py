class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        26 jul bottom up
        - return teh length of longest common subsequence
        - if no common return 0

        DP - each cell represents max common subsequence downards
        - each time you are at i1 and i2
            - if current are a match, +1
                - skip both
                note: no point trying to stagger i1 or i2 as this is greedy. might as well use the first occurence of match rather than later
            - else
                - i1 forward
                - i2 forward
        - each time get the surrounding max length of the above 3 cases cells
        
        base case
        does not need to end at the end to be complete. subsequence can be anywhere
        - reached out of bounds -> stop -> return 0 length
        - have an additional 0 padding

        - iterate from the bottom right base case



        Time:
        - O(l1 * l2) loop

        Space:
        - O(l1 * l2) matrix

        20 mins
        
        """
        # length1 = len(text1)
        # length2 = len(text2)
        
        # # let text1 be vertical by row, text2 horizontal column
        # # have an additional 0 padding for easy out of bounds return base case
        # dp = [[0] * (length2 + 1) for r in range(length1 + 1)]

        # for i1 in range(length1 - 1, -1, -1): 
        #     for i2 in range(length2 - 1, -1, -1):
        #         char1, char2 = text1[i1], text2[i2]
        #         if char1 == char2: # match
        #             dp[i1][i2] = dp[i1 + 1][i2 + 1] + 1 # diagonal 
        #         else:
        #             dp[i1][i2] = max(dp[i1 + 1][i2], dp[i1][i2 + 1]) # max between right or down
        
        # return dp[0][0]





        from functools import cache
        @cache
        def dfs(i1, i2): # return the max length for this index pair (DP)
            # base case
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            # current characters equal and valid
            if text1[i1] == text2[i2]:
                return dfs(i1 + 1, i2 + 1) + 1 # skip both
            else: # not valid, try move i1 or i2
                return max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))
        
        return dfs(0, 0)