class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        26 July 2026
        - return NO of expressions you can build that sum to target
        
        Questions
        - constraints of nums size
        - numbers are nonreplaceable -> unlike coin change
        - must be in order
        
        Idea
        - cannot do dfs(amount) as the number of diff expressions to form amount will be different depending on below:
            - the remaining digits available for use
            - that's why you need the remaining digit in the args for caching

        1)
        dfs(i, cur_sum)
        - base case
            cur_sum == target
                return 1
            cur_sum > target or i >= n:
                invalid return 0
        must use all element
        move + or move -


        2) 
        Bottom Up
        - sub problem -> return the no of ways to sum to target based on index of num and the current 
        - current_sum is spare and large -> use a defaultdict to represent the cols
            - dp[index][cur_sum] should give the no of ways

        Base case

        NOTE
        Because defaultdict is empty and is updated on the fly, the inner for loop will always be blank no iteration
        - so for i, you instead iterate on children, so i + 1 and reverse upwards to update the current i values in dp
                            i=3, cur_sum=3
                        -1/                  \+1
        i=4, cur_sum=2                          i=4, cur_sum=4
        assuming nums[3] = 1
        
        instead of normal main iterate y and inner iterate x to travel to the bottom and right dp to get it's current value at x, y
        - because you can't iterate through x as it is not known before hand how many columns there are as there is no fixed range. you need to go additional step down to reverse back up
        """

        from collections import defaultdict
        n = len(nums)
        ''' default dict as cur_sum is unlimited columns. So just key:value as cur_sum:no_of_ways'''
        ''' n + 1 to handle the base case of reaching out of bounds and the sum is target'''
        ''' if don't reach = no ways = default dict default 0 value'''

        dp = [defaultdict(int) for _ in range(n + 1)] 
        dp[n][target] = 1 # if it hit here, it is valid sum to total

        for i in range(n - 1, -1, -1):
            for cur_sum, ways in dp[i + 1].items():
                # reverse: if we had added nums[i], we'd have arrived at cur_sum
                dp[i][cur_sum - nums[i]] += ways
                # if we had subtracted nums[i], we'd have arrived at cur_sum
                dp[i][cur_sum + nums[i]] += ways

        return dp[0][0]















        """
        DP as you don't have to return the actual expressions but just the no. of possible

        At each step
        - choose minus or plus
        can't normal 1D dp as there will be no subproblem -> like you don't know what 
        values you need to form the sum -> so it's bruteforce and checking every possible
        combination like a backtracking
        O(2^n)

        cancel last - normal 2^n tree and you can use DP to solve subproblems
        - just need to keep track of the index and the sum

        - For each step find the complement of the current negative and positive
        - If it 

        Visualise tree
        - 2 branch for + and -
        - Every branch depth goes through every num
        """



        # ---------------------------- Brute Force ----------------------------
        # n = len(nums)
        # def backtracking(i, cur_sum):
        #     num = nums[i]
        #     if i == n - 1:
        #         # Could try return the count or use a nonlocal variable to keep track
                # This does not work as if both + and minus is the target, you must count both
        #         return 1 if (cur_sum + num == target or cur_sum - num == target) else 0
        #     count = (
        #         backtracking(i + 1, cur_sum + num) +
        #         backtracking(i + 1, cur_sum - num)
        #     )
        #     return count
        
        # return backtracking(0, 0)


        from functools import cache

        n = len(nums)

        @cache
        def backtracking(i, cur_sum):
            if i == n:
                return 1 if cur_sum == target else 0
            num = nums[i]
            return (
                backtracking(i + 1, cur_sum + num) +
                backtracking(i + 1, cur_sum - num)
            )

        return backtracking(0, 0)