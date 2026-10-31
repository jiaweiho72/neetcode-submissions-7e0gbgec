class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        1 Nov 2026
        find min in rotate array
        
        idea
        binary search -> sorted
        - split left region and right region
            - if left region
                min would be on the right region
            - if right region
                min would be in the region but you move left
            this only works if it is rotated, else the min is just the leftmost

        compare using the right side as your mid is biased to use the left pointer 
        - this would have edge case where it compare with itself

        you can't guaranteee the last visited is the min element, you may reach it in the middle
        and algo will continue searching
        """

        n = len(nums)
        l, r = 0, len(nums) - 1
        min_element = float('inf')

        while l <= r:
            m = (l + r) // 2        
            if nums[l] < nums[r]: # not rotated -> left is min
                min_element = min(nums[l], min_element)
                break
            
            # in the right region -> continue search on left
            if nums[m] < nums[r]:
                r = m - 1
                
            else: # left region -> min is on the right side
                l = m + 1

            min_element = min(min_element, nums[m])

        return min_element

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

