class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        27 Aug 2026
        logn -> binary search

        bruteforce
        - O(n) go through every element

        binary search
        - find target
        - if can't find target, return the last mid -> closest to target
        """
        n = len(nums)
        l, r = 0, n - 1
        correct_position = 0
        
        while l <= r: # == to handle odd -> need to still check if the odd == target
            """
            when reach here, target is not guaranteed to be in this range
            - if ODD and single element now
                [1] l,r,m = 0,0,0
                if target = 0 -> l,r=0,'-1' (OOB)
                if target = 2 -> l,r'='1',0 (OOB)

                l is the correct index to insert

            - if EVEN
                [1,2,3]
                [1,3], l,r,m = 0,1,0
                if target = 0 -> l,r=0,'-1' (OOB)
                if target = 2 -> l,r='1',1 (OOB)
                if target = 5 -> l,r='1',1 (OOB)

            why l is correct 
            - When the loop ends, l is exactly the first index whose value is NOT less than target
            odd:
            - 
            - mid bias going the left in even
            """
            m = (l + r) // 2 # bias the left side
            if nums[m] == target:
                return m
            elif nums[m] > target: # need to decrease -> move left
                r = m - 1
            else:
                l = m + 1
                

        return l 


