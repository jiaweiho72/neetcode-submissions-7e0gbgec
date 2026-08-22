class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        Now the merge is on array which can do in O(1) space. Cause string creates a new string with every object
        note: input has no duplicates

        merge sorted order
        - it is hard to merge from the front as it is hard to inplace change and keep track of nums1
        - solution: iterate from the back and get the max instead

        """

        i1, i2 = m - 1, n - 1 # start from the back
        insert_index = m + n - 1
        
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]: # insert the max
                nums1[insert_index] = nums1[i1]
                i1 -= 1
            else:
                nums1[insert_index] = nums2[i2]
                i2 -= 1
            insert_index -= 1
        
        # if there is still remaining nums1, it is ALREADY there, no need to insert
        # just need to handle for nums2
        while i2 >= 0:
            nums1[insert_index] = nums2[i2]
            i2 -= 1
            insert_index -= 1


            









        