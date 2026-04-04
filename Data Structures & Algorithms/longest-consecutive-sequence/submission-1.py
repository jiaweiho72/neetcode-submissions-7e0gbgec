class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        4 apr 2026
        * the order does not matter in the original array, just make a sequence
        - Bruteforce
            - sort the elements O(nlogn) 
            - for an element you do a long search and once break, start the search on the next element to the right of the break

        - optimal O(n)
            - starting of sequence -> previous element would not exist
                - if we only start from the start of sequence -> removes the repeated work
                - worst case if all numbers are unique, still O(n)
                    - if whole list is one sequence -> also O(n)
            - not sorted like in the brutforce so can't continue from the previous end
            - O(2n)
                - for each element it will iterate somemore. But the somemore sum up to n

        
        - return length of longest consecutive sequence
        """

        max_length = 0
        n = len(nums)
        nums_set = set(nums)

        for i in range(n):
            cur = nums[i]
            if cur - 1 not in nums_set: # start of seq
                cur_length = 1
                while cur + 1 in nums_set:
                    cur_length += 1
                    cur += 1
                max_length = max(max_length, cur_length)

        return max_length

