class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        
        - Same as rob1 but because it is cirular, try with skipping first and another with skipping last
        edge case
        if len(nums) <= 2:
            return max(nums)
        """

        from functools import cache

        if len(nums) <= 2:
            return max(nums)
        def rob1(nums):
            n = len(nums)
            @cache
            def dfs(i): # return the max money at index
                if i > n - 1: # out of bounds
                    return 0
                return max(dfs(i + 2), dfs(i + 3)) + nums[i]
                
            return max(dfs(0), dfs(1))
        
        return max(rob1(nums[:-1]), rob1(nums[1:]))