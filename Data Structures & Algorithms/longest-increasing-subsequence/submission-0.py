class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        25 jul 2026
        - return length of longest strictly increasing subsequence
            - can skip terms
            - in order
        
        idea
        - for each element
            - calculate the longest increasing subsequence from it
            - repeating subproblem:
                - you can cache the longest increasing at the index i
                    but it must be based on the prev index the value will change
                    - 
        issue with memoisation
        - memory issue
        - 2D, you need the longest increasing from that index
            - but there are different 

        need to run dfs starting on every node as it may not be it start at 0 or 1 or 2 or ...
        Constraints
        10^4 -> nlogn

        if used choose/don't choose dfs(i, prev_index) search space = O(n^2)

        Time: O(n^2)
        - dfs(i) n search space
            - for loop of n in each
        Space: O(n)
        - recursion stack n
        
        """
        from functools import cache
        n = len(nums)

        @cache
        def dfs(i): # return the max incr subsequence
            # base case
            if i >= n: # out of bounds got no element
                return 0

            # try every neighbour i onwards
            cur_max = 1 # include i itself
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    cur_max = max(cur_max, dfs(j) + 1)

            return cur_max

        return max(dfs(i) for i in range(n))


            

            
            











        """
        DP - bottom up
        - dp[index] = max(1, 1 + dp[index + 1] .... , 1 + dp[index + n - 1])
        - At every step, you are calculating for the index, the max subsequence length
        you can get if you start at that index. 1 is if it just stops at the index
        - return the max of the dp -> as you are trying all possible starting points

        O(n^2) compared to brute-force O(2^n)
        
        note: You shouldn't immediately accept when a num is larger as it may hinder an
        increasing sequence after it, if it's too large

        """
        n = len(nums)
        dp = [1] * n

        # O(n^2)
        for i in range(n - 1, -1, -1):
            # i + 1 as you are not searching for current i
            for j in range(i + 1, n):
                # If can maintain the increasing order, then check it
                if nums[i] < nums[j]:
                    # remember to + 1 as you are adding current element to the length
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # return the max of all possible starting points
        return max(dp)