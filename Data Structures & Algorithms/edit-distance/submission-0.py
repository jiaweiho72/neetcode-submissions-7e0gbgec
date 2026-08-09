class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Let:
        m=len(word1)
        n=len(word2)
        Time Complexity: O(m × n)
        Space Complexity: O(mn) memo table + O(m+n) recursion stack
        """

        from functools import cache
        @cache
        def dp(i: int, j: int) -> int:
            # Base cases
            if i == len(word1):
                return len(word2) - j  # insert remaining characters of word2
            if j == len(word2):
                return len(word1) - i  # delete remaining characters of word1
            
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)  # characters match, move forward
            else:
                # Try insert, delete, replace
                insert = 1 + dp(i, j + 1)
                delete = 1 + dp(i + 1, j)
                replace = 1 + dp(i + 1, j + 1)
                return min(insert, delete, replace)

        return dp(0, 0)





        """
        Bottom Up DP
        """
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][n] = m - i

        for j in range(n + 1):
            dp[m][j] = n - j

        # Fill table backwards
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert = 1 + dp[i][j + 1]
                    delete = 1 + dp[i + 1][j]
                    replace = 1 + dp[i + 1][j + 1]

                    dp[i][j] = min(insert, delete, replace)

        return dp[0][0]
    