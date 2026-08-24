class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        - there are negative numbers so sliding window may not work (idea
        where you iteratively add the right side and only decrement the left if 
        it exceeds k) because num maybe + or - so decrement left may instead increment

        1) bruteforce O(n^2)
        - for each num, check every other num and check sum

        2) bruteforce 2 - prefix sum
        - calculate the prefix sum at every index
        - but still bruteforce, you have to check every possible sub array O(n^2)

        3) Optimal idea
        - intuition: eg. [1,-1,1,1,1,1] and k = 3
            - at each index, you can determine the no of possible sub arrays by the complement
            - eg. index 4
                - the sum is 1-1+1+1+1+1 = 4
                - complement = 4 - 3 = 1
                    - no of prefix_sums which is 1
                        1 or 1-1+1
                    - so on the right side, it can either form -1+1+1+1+1 = 3 or 1+1+1 = 3
                    - if not possible, immediate ignore

        - implementation
            - a dictionary of prefix_sum: count
            - at each index, complement_prefix_sum = cur_prefix_sum - k
                - get count of complement_prefix_sum 
                    -> no of prefix sum = to this diff 
                    -> no of subarrays that sum to k where the subarray ENDS on this index
                    -> [xxxk] the xxx is no of prefix sums of the complement and k is the sum connecting to current index
            - considerations
                - 3-3 = 0 is valid. so initialise a 0 in the dict
                - you must fill the prefix_sum as you go.
                    - does not make sense you get prefix_sum in one pass where the count of x includes
                    points beyond the current index, you want the count before current index

        Time: O(n)
        Space: O(n) dict
        """

        n = len(nums)
        prefix_sum_count = {0: 1} # if k - k = 0, it is a valid one count
        cur_presum = 0
        result = 0

        for i in range(n):
            cur_presum += nums[i]
            complement_presum = cur_presum - k
            
            complement_count = prefix_sum_count.get(complement_presum, 0)
            result += complement_count # no of valid subarrays including nums[i]

            prefix_sum_count[cur_presum] = prefix_sum_count.get(cur_presum, 0) + 1
        return result









