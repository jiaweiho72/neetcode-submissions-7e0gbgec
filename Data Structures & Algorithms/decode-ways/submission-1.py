class Solution:
    def numDecodings(self, s: str) -> int:
        """
        25 July 2026
        - return NO OF WAYS to decode
        - may not have solution -> return 0
        - number is the 1-index in the alphabet
        notes: 06 invalid

        Idea
        - have a 'int': letter map
            - actually don't need as you don't need to return the actual substring
        - go through every char in s
            - each time try a combination
                - single digit
                    - cannot be 0, invalid, early return
                - double digit
                    - check if it under 26
                    - do not include if 0 is in front

        so will do a dfs: returns the no of ways
        - two ways about -> O(2^n)
        - repeating subproblem, if I already calculated i onwards have how many ways, just reuse -> cache

        note: all are strings
        Time: Cache O(n)
        space: recursive stack O(n)
        20 mins

        mistake: early returned the second digit check. If the single digit check was valid but because second digit check was invalid, it return 0 which is wrong, should return the single one at least
        """

        n = len(s)
        from functools import cache

        @cache
        def dfs(i): # return no of ways
            # base case
            if i == n:
                return 1
            if i > n:
                return 0

            cur_digit = s[i]
            if cur_digit == "0": # It will just not count that path -> return zero ways
                return 0

            # 1) Handle single digit
            single_ways = dfs(i + 1)

            # 2) Handle double digit
            double_ways = 0
            if i + 1 in range(n):
                double_digit = s[i:i + 2]
                if int(double_digit) <= 26: # valid alphabet
                    double_ways = dfs(i + 2)

            return single_ways + double_ways
            
        return dfs(0)
