class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        26 July 2026
        - return the max profit
            - as many transactions as you like
            - after selling a stock you cannot buy in the next day
        difference with other question
        - nonlinear greedy localoptimal!=gloabloptimal decision, you multiple possible decisions at each point

        note: you must sell before you buy again

        idea - trying everything
        DFS - returns the max profit if bought or not bought at that point onwards
        - when you buy, you can't buy again so you need a flag
            - you can only choose to hold
            - or sell and wait i + 1 day
        - when not bought
            - you can choose to buy or not buy current
        - base case
            - out of range -> no profit 
        any repeated case?
        yes


        Time:
        - dfs cache states = n * 2, no of prices * boolean
        Space
        - recursive stack, cache O(n)

        Constraints
        n <= 5000 -> n^2
        """
        n = len(prices)
        from functools import cache
        
        @cache
        def dfs(i, is_bought): # return max profit
            if i >= n:
                return 0
            if is_bought: # currently bought -> only can sell
                # 1) Hold; 2) Sell and cooldown
                return max(dfs(i + 1, True), dfs(i + 2, False) + prices[i])
            else: # can buy or don't buy
                # 1) Don't buy first; 2) Buy
                return max(dfs(i + 1, False), dfs(i + 1, True) - prices[i])
        
        return dfs(0, False)
