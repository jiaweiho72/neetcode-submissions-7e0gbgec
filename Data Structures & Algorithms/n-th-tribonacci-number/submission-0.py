class Solution:
    def tribonacci(self, n: int) -> int:
        """
        24 Aug 2026
        - Tribonacci
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