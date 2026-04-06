class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        return no of ways

        * inclusive of n
        '''
        from functools import cache

        # @cache
        # def dfs(i):
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1

        #     return dfs(i + 1) + dfs(i + 2)
        # return dfs(0)


        """
        each step -> no of ways to reach i steps
        * fibonacci but n + 1
        """
        # @cache
        # def dfs(i):
        #     if i < 2:
        #         return i
        #     # add no of ways from i - 1 and i - 2
        #     return dfs(i - 1) + dfs(i - 2)

        # return dfs(n + 1)



        """
        7 apr

        """
        from functools import cache
        @cache
        def dfs(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            return dfs(num - 1) + dfs(num - 2)
        return dfs(n + 1)


        