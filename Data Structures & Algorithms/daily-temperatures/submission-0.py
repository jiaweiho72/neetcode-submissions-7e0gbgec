class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        4 apr 2026
        - return result array where i is no of days after the ith day before a warmer temp appears
            - if no warmer -> set to 0

        idea
        - monotonic decreasing stack
            - keep adding to stack if the temp is less than or equal (decreasing)
            - if hit higher -> mark that as the first warmer weather for all the previous days in the stack
                - pop them off to not process them in again
                - thus, you need to keep track of index too
        """

        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            cur_temp = temperatures[i]
            while stack and cur_temp > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append((cur_temp, i))

        return result