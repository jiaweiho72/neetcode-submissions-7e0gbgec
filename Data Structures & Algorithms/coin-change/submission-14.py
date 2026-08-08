class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom up test
        """

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                complement = a - c
                if complement >= 0: # Ensure no negative numbers
                    dp[a] = min(dp[a], dp[complement] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1



        

        """
        25 Jul 2026
        - return FEWEST no of coins to make up amount
        - if not possible return -1
        - infinite number of coins

        questions
        - infinite, can repeat coins

        idea
        - dfs: returning the min no of coins to make up that amount
            - for amount
                - see for each coin the complement (amount - coin)
                    then dfs on that to get the min coins to make up this complement
        - repeated problems where A is already calculated -> DP

        - it's hard to catch the negative complement case in the dfs basecase
            - as you need to return an IDEA that it is invalid. 
            - return 0 is considered valid, so you need additional variables
            - easier to do before calling


        Time:
        - O(n) from DP
        Space:
        - O(n) recursive stack
        """
        from functools import cache

        @cache
        def dfs(amt):
            # base case
            if amt == 0: # valid as equal to amount: 0 no of coins needed to build 0
                return 0

            min_amt = float('inf')
            for i in range(len(coins)): # infinite pool of coins
                coin = coins[i]
                complement = amt - coin
                if complement < 0: # ignore negative numbers
                    continue
                min_amt = min(min_amt, dfs(complement))
            return min_amt + 1
        
        min_coins = dfs(amount)
        return min_coins if min_coins != float('inf') else -1




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


