class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        sorted. Remove duplicates inplace. return no of unique elements such that first k values are the unique values

        the back, don't need to consider

        idea
        - two pointer, write position and the next position


        Time:
        O(n) - not nested loop, total is n
        Space:
        O(1) - no additional space
        """
        n = len(nums)
        write, read = 0, 0

        while read < n:
            while read + 1 < n and nums[read] == nums[read + 1]:
                read += 1
            nums[write] = nums[read]
            read += 1

            write += 1
        return write
