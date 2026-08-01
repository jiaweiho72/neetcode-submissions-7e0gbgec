class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        16 June 2026
        Kadanes algorithm
        can always get the max of the current point to the end. dont need dfs, greedy, subarray is contiguous
        """
        n = len(nums)
        max_sum = float('-inf')
        cur_sum = 0
        for i in range(n):
            if cur_sum < 0: # negative sum might as well start a fresh
                cur_sum = 0 
            cur_sum = nums[i] + cur_sum
            max_sum = max(max_sum, cur_sum)
        return max_sum