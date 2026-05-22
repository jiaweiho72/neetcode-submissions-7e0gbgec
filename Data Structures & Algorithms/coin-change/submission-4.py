class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # """
        # 7 apr 2026
        # - return fewest number of coins to make exact amount
        # - if impossible, return -1
        # - unlimited no of each coin

        # dfs around fewest no of coins to build current amount a
        # """

        # from functools import cache

        # n = len(coins)

        # @cache
        # def dfs(a): # returns min coin to get amount
        #     # base case
        #     if a == 0:
        #         return 0
            
        #     min_coins = float('inf')
        #     for i in range(n):
        #         coin = coins[i]
        #         complement = a - coin
        #         if complement >= 0: # negative means not possible
        #             min_coins = min(min_coins, dfs(complement))
        #     return min_coins + 1

        # min_coins = dfs(amount)
        # # if min still float, means, did not find a valid combination
        # return min_coins if min_coins != float('inf') else -1

        """
        23 May 2026
        - return min no of coins to make up exact target. If not possible return -1
        - unlimited no of each coin

        DP
        - logic: I can find the min no of coins to form a
        - repeated logic
        """
        from functools import cache
 
        @cache
        def dfs(a): # return the min for this amount
            # base case:
            if a <= 0:
                return 0
            
            min_coins = float('inf')
            for c in coins:
                # if use this coin
                complement = a - c

                if complement >= 0: # complement not negative
                    min_coins = min(min_coins, dfs(complement))
            return min_coins + 1
            
        result = dfs(amount)
        return result if result != float('inf') else -1












