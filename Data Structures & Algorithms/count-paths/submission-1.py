class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Speed Run
        output: no of unique paths from top left to bottom right

        Dynamic programming
        - sub problem is at every cell, what is the no of path to endpoint
        - at each step
            - move right
            - OR move down
            - invalid when out of bounds -> backtrack
            - base case when reach the bottom right
        
        """
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dfs(r, c):
            # If out of bounds
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            return dfs(r, c + 1) + dfs(r + 1, c)

        return dfs(0, 0)

