class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        25 sept 2026 - retry
        time: O(n)
        space: O(1)
        """
        n = len(nums)
        global_max, global_min = float('-inf'), float('inf')
        cur_max, cur_min = 0,0 # cur max and min sums starting from left
        total_sum = 0

        for i in range(n):
            # to keep get total sum
            total_sum += nums[i]

            # use or don't use previous. cur_max is the max sum of subarray on the left, including current elemnt
            cur_max = max(nums[i], cur_max + nums[i])
            cur_min = min(nums[i], cur_min + nums[i])

            global_max = max(global_max, cur_max)
            global_min = min(global_min, cur_min)

        """
        edge case if all negative
        - global_min will be sum of all numbers -> total - global_min = 0
            - then global max will be negative
            - this wrongly picks 0 as it is greater than the global_max which is negative
                - wrong as you have to pick at least one number (negative)
        - it is ok if at least one positive number as the global_max will be positive and 
        the answer will always be greater than this incorrect global_min
        """
        return max(global_max, total_sum - global_min) if global_max > 0  else global_max









        """
        24 Sep 2026
        - can't overlap the circular array
        - calculate max sum of circular subarray

        idea
        - no fixed size/window constraint -> need to try all -> not sliding window
            - even with prefix sum -> need to try all start and end points of all possible subarray
            - if it is finding target sum, can use hashset to check against if complement had a prefix sum            
        - maxsum subarray with non-negative -> just sum all
        - maxsum subarray with negative -> kadane algo
            - but need to ensure no overlap where item used more than once
            - if negative sum, might as well start from afresh
        bruteforce
        - n^2, start every position search for size n
            - sliding window where constraint is max size is n -> need to keep within
                - iterate up to 2n

        can you choose empty subarray if all negative? 
        - if all negative, choose the least negative number

        edge
        -10000, 1, 2, 4
        it is most optimal if i skip the -10000 and look at the rest
        if i check cur_sum < 0 before checking size > n:
            i will miss the case where I can use 1,2,4 as I only check 2,4

        mistake: in the pruning
        - need to remove the l element before you increment l
        - kadane works for non rotating array
            [-3,5,5] works as you will skip -3
            - always knows the optimal sum from current to the left
        - for rotating, [5,-3,5], the left varies now
        """
        n = len(nums) # max subarray size
        max_sum = float('-inf') # max sum may be negative
        cur_sum = 0

        l = 0
        for r in range(2 * n): # 0 to 2n - 1 -> won't overlap
            # we are guaranteed to use this right item
            if (r - l + 1) > n: # oversized -> cut left index 
                cur_sum -= nums[l % n]
                l += 1
            if cur_sum < 0: # if negative makes sum worse -> might as well don't use previous elements and start afresh
                cur_sum = 0 # reset to zero
                l = r # reset to current point
            
            cur_sum = max(nums[r % n], nums[r % n] + cur_sum)
            max_sum = max(max_sum, cur_sum)

        return max_sum 












