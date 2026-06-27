class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        28 Jun 2026

        - bruteforce: O(n^2) for every day try every other day
        - optimised: 
            - you want to min of the left side always
            - iterate only the right pointer. Update the left pointer if you find a value smaller than the min of the left side
                - it works cus you iterate through everything on the left and on the way
                    you get the left min at the current index
        """
        max_profit = 0
        l = 0
        n = len(prices)
        for r in range(n):
            if prices[r] >= prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else: # no profit
                l = r

        return max_profit



        """
        4 apr 2026
        notes
        - one day buy, another dat sell
        - return max profit 
        - can choose not to make any transaction -> profit 0

        idea - two pointer
        - left pointer is buy date
        - iterate over the right pointer
        - right pointer if > buy price -> sell -> note down profit
            - if the right pointer is < buy_price:
                - can 'buy' at this point instead for a larger profit

        - movement: iterate through right, left move only if find a smaller value
            - makes no sense to keep the old larger value
            - basically at any point -> you want the min of the left side
                - then you compare the max of the right side


        - note: I can't just find the max and min value as the sequence matters
            - though I could iterate and get the prefix min and postfix max per index
        
        12 min
        """


        n = len(prices)
        l = 0 # l is the current min
        max_profit = 0
        for r in range(1, n):
            cur = prices[r]
            if cur >= prices[l]: # try selling
                cur_profit = cur - prices[l]
                max_profit = max(max_profit, cur_profit)
            else:
                l = r # set new left side minimum
        return max_profit
            



            

        return max_profit


