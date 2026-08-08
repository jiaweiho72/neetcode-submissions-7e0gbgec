class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        26 Jul 2026
        Bottom Up test
        - return min cost to reach top floor
        - one or two steps

        idea
        - each i, it is the min cost to reach the top
        - try space optimised (no dp list)
            instead of dp[i + 1], store in a temp step 1
            - use the cost list to store

        base case
        - reach the top
        """

        n = len(cost)
        # don't need to check if n < 2 as it just won't run the for loop and the return will handle it
        
        # base case
        # no need as last two

        for i in range(n - 1 - 2, -1, -1):
            min_next_cost = min(cost[i + 1], cost[i + 2])
            cost[i] += min_next_cost
        
        return min(cost[0], cost[1])






        """
        23 Jul 2026
        - can either start at 0 or 1
        - get the min cost at index moving one step vs two step
        dfs
        - returning the min cost at that index
        - one or two steps

        Time: O(n) with cache
        Space: O(2n) recursive stack and cache
        """
        from functools import cache
        n = len(cost)
        @cache
        def dfs(i):
            if i >= n: # out of range
                return 0
            return min(dfs(i + 1), dfs(i + 2)) + cost[i]

        return min(dfs(0), dfs(1))
