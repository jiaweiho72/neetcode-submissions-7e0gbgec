class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import cache
        @cache
        def dfs(amt, i):
            if amt == 0:
                return 1
            if amt < 0 or i == len(coins):
                return 0

            # include current coin (stay on same index) + exclude current coin (move to next)
            return dfs(amt - coins[i], i) + dfs(amt, i + 1)

        return dfs(amount, 0)

        """
        26 July 2026
        - return no of combinations that make up amount
            - also infinite number of coins

        dfs(amt) - returns no of ways to make up this amount
        - repeat for every amt down
            - each time try every coin
                - get complement and call dfs(complement) if amt not negative
        - base case
            - amt = 0
                return 0
            - amt negative handled before calling

        Unlike Coin Change
        - coin change is just getting the min and there are permutations counted
            - 1+2 and 2+1 is counted
            - min has no problem because eventhough you accept both, you just get the mean
        - this case you are getting combination nor permutation (so you would count extra
        Why this happens: Your state is only amt. After choosing a coin, the next recursive call is free to choose any coin again, including smaller ones, which generates different orders of the same set.
        - FIX: add an index as arg
            - don't process the index before again
            example coins = [1,2] and amount = 3
            0 + 1 + 1 + 1
            0 + 1 + 2   (this will handle this combination)
            0 + 2 + 1 （prevented as you don't revisit coins before it, but can still visit 2)


        """

        """ below not working"""
        # from functools import cache
        # coin_length = len(coins)

        # @cache
        # def dfs(amt, coin_index): # return no of ways to make up amount
        #     if amt == 0:
        #         return 1

        #     no_of_ways = 0
        #     for i in range(coin_index, coin_length):
        #         complement = amt - coins[i]
        #         if complement >= 0:
        #             no_of_ways += dfs(complement, i)

        #     return no_of_ways
        
        # return dfs(amount, 0)











        # dp = [0] * (amount + 1)  # DP array to store the number of ways
        # dp[0] = 1  # There's exactly 1 way to make amount 0 (use no coins)

        # # Update each amount in the dp
        # for c in coins:  # Iterate through coins first
        #     for a in range(c, amount + 1):  # Start from `c` to ensure `a - c >= 0`
        #         dp[a] += dp[a - c]  # Add the ways to make amount `a - c`

        # return dp[amount]
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i, total):
            # base case: exact amount reached
            if total == amount:
                return 1
            # base case: over the amount or no coins left
            if total > amount or i == len(coins):
                return 0

            # include current coin (stay on same index) + exclude current coin (move to next)
            return dfs(i, total + coins[i]) + dfs(i + 1, total)

        return dfs(0, 0)