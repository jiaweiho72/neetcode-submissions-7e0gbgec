class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        4 apr 2026
        - input sorted
        - ouput: min element of array


        # not finding target, finding min
        - binary search logn 
            - determine m is which side of the rotated array (m compare with l)
                - if m is more than l -> left side
                - if m is less than l -> right side
                - if l < r -> unrotated

        18 mins
        """
        n = len(nums)
        l, r = 0, n - 1
        min_num = float('inf')
        while l <= r:
            m = (l + r) // 2

            # check current is rotated or not
            if nums[l] < nums[r]:
                min_num = min(min_num, nums[l]) # may not be the min but a candidate
                break

            elif nums[m] >= nums[l]: # left region -> look right
                l = m + 1

            elif nums[m] < nums[l]: # right region -> look left
                r = m - 1
            
            min_num = min(min_num, nums[m])

        return min_num

