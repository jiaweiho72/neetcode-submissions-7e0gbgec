class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        30 Aug 2026
        - return smallest positive integer not in nums
        - implement in O(n) time and O(1) space

        bruteforce
        - sort and find the first time a gap is found, return answer O(nlogn)
        - try even number from 1 to len(nums) + 1. O(n)
            - eventhough num can be infinity
            - the empty space to slot new number in is at most len(nums) + 1 (end of array)
            - use hashset to keep track if used before O(n) space

        observation
        - if num > len(nums) + 1. won't be relevant and can ignore

        Optimal
        - in place keep track of a list where you insert to an index == num
            - 1indexed
            - but issue is that you corrupt haven't visited elements
                - solution: let the index of array represent the number
                    keep the value in the list but have a flag to label the index whether it has been found
                    - use negative to mark that it was found in the list
                    - make sure ACTUAL negative numbers are set to 0 to ignore
                        - need a separate iteration first because you can't update in real time both
                            - setting negative to 0 as well as setting negative label. will conflict
        - second pass to find for 1 to len(nums) 1-indexed whether it exists in the array (check if value negative)
            - the actual value in the list don't mean anything anymore
        
        pitfall
        - don't do [-n for n in nums] shortcut as it creates new list. Instead inplace update
        - off by one
            - let nums be 1-indexed
            actual num need to -1 for index
            - the max possible result range ends at len(n) index which is out of range. But it is ok,
            just need to check the previous value only
        - edge case where you try to set negative, but value is 0. is pseudo -1
            - not value at that point may be positive or negative, just can't be 0

        basically instead of hashmap to check if element exists:
        - *special case where result set is the length of the list*
        - so we can use the list index and a negative flag as a replacement to check if element exists in list
        
        
        Time: O(3n)
        Space: O(1)
        """

        n = len(nums)

        # 1) First pass: reset all negative values to 0
        for i in range(n):
            if nums[i] < 0: # if negative, reset to 0 to ignore
                nums[i] = 0

        # 2) Second pass: label the nums that were found, it's corresponding index value to negative
        for i in range(n):
            num = abs(nums[i]) # may have been updated in earlier steps
            index = num - 1 # nums is 1-indexed in idea. Actual index -1
            if 0 <= index < n: # within range (ignore 0 -1 from step 1)
                nums[index] = - abs(nums[index] if nums[index] != 0 else -1) # set negative

        # 3) Third pass: Check all possible result value from 1 to len(nums) + 1
        for i in range(n):
            if nums[i] < 0: # negative -> present in nums
                continue
            else: # first encounter where not present in nums
                return i + 1 # 1-indexed
        
        # reach here means every element present in list -> answer is next element after last -> len(nums) + 1
        return n + 1

            









