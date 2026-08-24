class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        24 Aug 2026
        - return min length of subarray whose sum >= target
        - return 0 if no such subarray
        note: positive numbers

        idea
        - contiguous subarray of fixed condition (sum <= target) -> sliding window
        - constantly check for the min_length
        - this sliding window does not need to init as the size is not fixed. condition is not the size but the sum property
        """

        n = len(nums)
        l = 0
        min_length = float('inf')
        cur_sum = 0

        for r in range(n):
            cur_sum += nums[r]
            while cur_sum >= target: # while still valid -> decrement the left side
                min_length = min(min_length, r - l + 1) # it has been checked that cur_sum >= target
                
                cur_sum -= nums[l]
                l += 1

        return min_length if min_length != float('inf') else 0
