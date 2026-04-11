class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        11 Apr 2026
        - can't rob two adjacent houses
        - return max amount of money without alert police

        - try every path moving 2 or moving 3
            - can't move 1 as alerts police
            - there is no need to simulate 'skip' a move as it is greedy
                - if you choose to move 4, it would have been better to move 2 2
        - sub problem
            every index, you can already know the max amount further down the path
        """

        from functools import cache

        n = len(nums)

        @cache
        def dfs(i): # returns max amount from this index onwards
            if i >= n: # out of bounds
                return 0
            return max(dfs(i + 2), dfs(i + 3)) + nums[i]

        # There is no move 1 so need to account for 1 too
        return max(dfs(0), dfs(1)) 





