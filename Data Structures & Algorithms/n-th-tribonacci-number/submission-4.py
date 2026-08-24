class Solution:
    def tribonacci(self, n: int) -> int:
        """
        space optimised
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        first, second, third = 0, 1, 1

        for i in range(3, n + 1):
            nxt = first + second + third
            first, second, third = second, third, nxt

        return third







        """
        Bottom Up
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]

        """
        24 Aug 2026
        - Tribonacci

        Time: O(n)
        Space: O(1)

        5:32 mins
        """
        from functools import cache

        @cache
        def dfs(i): # return trib sum
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            return dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
        
        return dfs(n)






        
 





