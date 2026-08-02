class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        1 aug 2026
        - return the median of two sorted arrays

        idea
        - Bruteforce
            merge sort the arrays and get the middle O(m + n)
        - Optimal
            - instead of merging
            - choose an index in nums1 which partitions it into two parts
                - with the hopes that this splits left and right as median
                - use binary search to try different indexes
            - as we know median is 1/2 total size -> from nums1 index, we can get nums2 index
                - so just do binary search on one nums1
            - choose the smaller arr
                - faster search area 
                - you wont have OOB when indexing the other array
                    eg. nums1 = length 100; nums2 = length 2
                    m1 = 80; m2 = -40 (too far out)

            - binary search decisions
                - mid = partition
                    - let left be mid and right be mid + 1
                        edge case: all elements chosen are from one array and not mixed
                            - so the unused array the m will be -1 
                        - to ease validation -> if one pointer is out of bounds -> set infinity
                    - as we know within nums1, since it is sorted, left always < right
                        - so we just check cross arrays
                        - left1 < right2 and left2 < right1
        [1 2 3 | 4 5 6]

        """
        # work on shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total_length = len(nums1) + len(nums2)
        half_length = total_length // 2
        l, r = 0, len(nums1) - 1

        while l <= r:
            m1 = (l + r) // 2 # mid is the partition point in nums1
            m2 = half_length - m1 - 2

            """
            set nums1/nums2 left/right edge indexes
            - eg. total = 8, half = 4
                - if nums1 takes all half:
                    l1 == 3; r1 4 (OOB)
                    l2 == 4-3-2 = -1 (OOB); r2 == 0
            - just need to set a value else nums1[m1] OOB
            """
            left_val1 = nums1[m1] if m1 >= 0 else float('-inf')
            right_val1 = nums1[m1 + 1] if m1 + 1 < len(nums1) else float('inf')
            left_val2 = nums2[m2] if m2 >= 0 else float('-inf')
            right_val2 = nums2[m2 + 1] if m2 + 1 < len(nums2) else float('inf')

            # Validate
            if left_val1 < right_val2 and left_val2 < right_val1: # won't be equal as distinct elements?
                """
                Return the median:
                - we have not compared left_val1 and left_val2 and same for right
                - if odd:
                    return min of the right side (it will be one of the right)
                    - why right:
                        - eg.
                            1 2 3 4 5
                            half = 5 // 2 = 2
                            1 2 | 3 4 5

                        because use floor division, the left will the mid?                
                - else even:
                    get the average between the max of left and min of right
                    /2 because answer wants decimal too
                """
                if total_length % 2 == 1: # odd
                    return min(right_val1, right_val2)
                else:
                    return (max(left_val1, left_val2) + min(right_val1, right_val2)) / 2
            # continue binary search
            else:
                if left_val1 > right_val2: # 1 is too big, need to decrease size -> shift left
                    r = m1 - 1
                else:
                    l = m1 + 1
                
                









        """
        30/09/25

        Idea
        - Focus on finding the 1st half of the median
        - Binary search on the smaller array A
            note: just need BS on one array as you can get the other part from (half-m)
                - A now from 0 to m
                - B now from 0 to (half - m)
                - smaller is better as you have less area to search -> faster
            - Validate if current partition is valid
                - valid:
                    - cross check: eg. for A, check m is indeed smaller than B's (half-m) + 1. 
                        Vice versa for B
                    - edge case: all elements chosen are from one array and not mixed
                        - to ease validation -> if one pointer is out of bounds -> set infinity
                    - once valid:
                        - handle odd case:
                            - median is just the min of the next elements in A and next in B
                        - handle even case:
                            - get max of the left side of A and B
                            - get the min of the right side of A and B
                            - median is the average of the two values
                - invalid:
                    - if A left is larger than B right
                        -> you need to reduce elements in A (smaller elements)
                        -> move r to the left
                    - else:
                        -> you need large elements from A
                        -> move l infront
        """

        # 1) We will work on the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        # 2) Binary search for short
        l, r = 0, len(nums1) - 1
        while l <= r + 1:
            # m and m2 are the end index of the selected left half of median
            m1 = (l + r) // 2
            m2 = half - (m1 + 1) - 1

            """
            Gets the rightmost elements in the left partition and the leftmost in the right patition
            - basically the middle values touching each other
            NOTE: l is now the value and not the index -> for ease as it's value is frequently used
            """
            l1 = nums1[m1] if m1 >= 0 else float('-inf')
            r1 = nums1[m1 + 1] if (m1 + 1) < len(nums1) else float('inf')
            l2 = nums2[m2] if m2 >= 0 else float('-inf')
            r2 = nums2[m2 + 1] if (m2 + 1) < len(nums2) else float('inf')

            # Validate
            if l1 <= r2 and l2 <= r1: # valid
                if total % 2 == 1: # Odd case
                    return min(r1, r2)
                # Even case
                return (max(l1, l2) + min(r1, r2)) / 2
            else: # continue binary search
                if l1 > r2:
                    r = m1 - 1
                else: # long_left > short_right
                    l = m1 + 1