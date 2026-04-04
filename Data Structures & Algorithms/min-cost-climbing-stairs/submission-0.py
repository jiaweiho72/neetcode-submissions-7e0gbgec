class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # Brute force but optimised with bottom up DP

        # # At each index, is the min cost to reach the end
        # n = len(cost)
        # # take one step or take two step from position
        
        # cost.append(0)
        # """
        # Visualising:
        # - Even at the last element in cost, that is the cost to reach a imaginary endpoint
        # outside of the list.
        # - So you should update `cost` with the min cost to reach the imaginary at that point

        # ignore last element as that is just the cost to reach end alr
        # minus another one cus you add 0
        # - regular reverse iteration is (n-1,-1,-1)
        # """
        # for i in range(n - 3, -1, -1):
        #     move_one_cost = cost[i] + cost[i + 1]
        #     move_two_cost = cost[i] + cost[i + 2]
        #     cost[i] = min(move_one_cost, move_two_cost)
        # return min(cost[0], cost[1])


        """
        Each index is the position and value is the min at that index
        """
        # n = len(cost)
        # dp = [float('inf')] * n 
        # dp[n - 1] = cost[n - 1]
        # dp[n - 2] = cost[n - 2]
        # for i in range(n - 3, -1, -1):
        #     # min between choosing to go one step or two steps
        #     move_one_cost = cost[i] + dp[i + 1]
        #     move_two_cost = cost[i] + dp[i + 2]
        #     dp[i] = min(move_one_cost, move_two_cost)
        # return min(dp[0], dp[1])

        """
        Speed run
        - at each point, return the min cost
        """
        # from functools import lru_cache
        # n = len(cost)

        # @lru_cache(maxsize=None)
        # def dfs(i):
        #     # base
        #     if i >= n: # reach outside
        #         return 0

        #     # Get min cost between two options - 1/2 steps
        #     return min(dfs(i + 1), dfs(i + 2)) + cost[i]
            
        
        # return min(dfs(0), dfs(1)) # start at 0 or 1

        """
        Grad alr
        DFS
        - at every step
            - take 1 or 2 steps
        - base case:
            - out of bounds
        - return:
            - min cost

        sub problem
        - at position, the min cost to get from it to the end

        * top is after the last ele
        """

        n = len(cost)
        def dfs(i):
            if i >= n:
                return 0

            return min(dfs(i + 1), dfs(i + 2)) + cost[i]

        return min(dfs(0), dfs(1))


