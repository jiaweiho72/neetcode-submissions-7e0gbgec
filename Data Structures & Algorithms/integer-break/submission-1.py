class Solution:
    def integerBreak(self, n: int) -> int:
        """
        25 Oct 2026
        - given integer n, break into sum of k integers where k >= 2.
        - maximise product of integers (DP)
            - optimisation: each dfs can return a specific optimal value, instead
            of each dfs(x) with different paths has multiple values and dk which one to use
        
        idea
        - form amount sum k
            - return the max product to form sum k
        n^2

        - dfs(sum) -> return max product
            - for i in range(n):
                - try dfs(complement)
            - return the max
        """

        from functools import cache
        
        @cache
        def dfs(cur_sum):
            if cur_sum == 0:
                return 1

            cur_max_product = 1
            for i in range(1, n): # don't allow 0 and n to prevent just not splitting into k >=2
                complement = cur_sum - i
                if complement < 0:
                    break # not continue, as any large i won't be in range

                cur_max_product = max(
                    cur_max_product,
                    dfs(complement) * i
                )
            return cur_max_product

        return dfs(n)








