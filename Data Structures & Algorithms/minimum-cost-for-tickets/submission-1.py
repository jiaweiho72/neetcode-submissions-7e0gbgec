class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        23 July 2026

        DP
        - dfs(i) return the min cost to travel from i onwards
            - each iteration
                - move 1, 7 or 30
                    - find the exact next day index by finding the nearest to it
        """

        n = len(days)

        from functools import cache
        @cache
        def dfs(i):
            # base case
            if i >= n: # out of bounds -> could complete the trip (as overshot)
                return 0 # no cost

            cur_day = days[i]
            # choose 1 day pass
            cost1 = dfs(i + 1) + costs[0] # meaning: buy pass today, process the next travel day

            # choose 7 day pass
            # to find the next travel day that is not ALR covered by this 7 day pass
            temp_idx = i
            while temp_idx < n and cur_day + 6 >= days[temp_idx]: # -1 as inclusive of cur_day
                temp_idx += 1
            cost2 = dfs(temp_idx) + costs[1]


            # choose 30 days
            temp_idx = i
            while temp_idx < n and cur_day + 29 >= days[temp_idx]:
                temp_idx += 1
            cost3 = dfs(temp_idx) + costs[2]

            return min(cost1, cost2, cost3)

        return dfs(0)




