class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        1 Nov 2026
        - return true if can partition into two subsets equal

        idea
        - bruteforce
        - dfs(i, cur_sum) backtracking
        - optimal is form the amount and cache by that, whether 

        return boolean if can form the sum from i

        top down needs 2D

        still, it needs the current element element and the next j
        """


        from functools import cache

        n = len(nums)
        total = sum(nums)
        if total % 2 != 0: # not even -> not valid
            return False
        half_target = total // 2 # returns int rather than float

        @cache
        def dfs(i, cur_sum):
            if cur_sum == half_target:
                return True
                
            for j in range(i, n):
                # early return skips
                if cur_sum + nums[j] > half_target:
                    continue
                if dfs(j + 1, cur_sum + nums[j]):
                    return True
            return False

        return dfs(0, 0)
                


                









        """
        Dynamic programming
        - choose to add in sum1 or sum2
        - key: you just need a subset that sum to half the total sum
        - return boolean at each point
        """
        from functools import cache
        total = sum(nums)

        # If total is odd, can't split evenly
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        @cache
        def dfs(i, cur):
            if cur == target: # Found a subset
                return True
            if i >= n or cur > target: # Out of bounds or overshoot
                return False
            # Choice: take nums[i] or skip it
            return dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)

        return dfs(0, 0)



        """
        Bottom Up: Dynamic programming
        dp[i][cur] = current sum after using until i elements
        """
        total = sum(nums)

        # If total is odd, can't split evenly
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[n][target] = True

        for i in range(n - 1, -1, -1):
            for cur in range(target + 1):
                # Choice: take nums[i] or skip it
                if cur + nums[i] <= target:
                    dp[i][cur] = dp[i + 1][cur + nums[i]] or dp[i + 1][cur]
                else: # skip to keep cur_sum < target
                    dp[i][cur] = dp[i + 1][cur]

        return dp[0][0]






        """
        25 Jul 2026
        Testing for loop method
        - return true if can partition into two subsets where sum in both is equal
            - false otherwise
        impt: subset, is set, so no order, no contiguous

        idea
        - for every element
            - try choose or don't choose the set
            - need to get sum of both sides quick
                - DEPREATED prefix sum -> allows to get sum of range instantly by index
                - just along the dfs, get the sum
        hack: just need to check one side and ensure it  total/side = 2


        must include dfs(i, cur_sum)
        - it returns whether i onwards can form a valid half subset, given the current sum
        """

        from functools import cache
        n = len(nums)
        total_sum = sum(nums)

        # If total is odd, can't split evenly
        if total_sum % 2 == 1:
            return False
        target_sum = total_sum // 2
        
        @cache
        def dfs(i, cur_sum):
            cur_sum += nums[i]
            if cur_sum > target_sum:
                return False
            if i == n - 1 and cur_sum != target_sum:
                return False
            if cur_sum == target_sum:
                return True
            for j in range(i + 1, n):
                if dfs(j, cur_sum):
                    return True

            # False until proven true
            return False

        for i in range(n):
            if dfs(i, 0):
                return True

        return False
            






