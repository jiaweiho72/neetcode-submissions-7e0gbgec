class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        29 Aug 2026
        - may have duplicates
        - may be unrotated if rotated n times
        diff vs I, duplicates -> skip them if possible

        return true if target is in nums else false -> binary search

        check mid on the left side or right rotated side
        - if left side:
            - when to search left
                - target < mid and target > leftmost
                
            - when to move right
                - target < mid and target < leftmost (on the right rotated)
                - target > mid
                    - guranteed on the left rotated side
        may not be rotated at points

        [2,3]
        [3,2]
        """


        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return True
            
            # 1) if left region
            if nums[m] > nums[r]: 
                '''
                m == r only on odd case; if you used l, there will be [2,3] or [3,2] even case where
                m == l and both cases it reaches this condition!! which is inaccurate
                '''
                if target < nums[m] and target >= nums[l]: # only case you look left. All else look right
                    r = m - 1
                else:
                    l = m + 1
            
            # 2) else right region
            elif nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
            # 3) equal - duplicate or base even case. Duplicate means from m to r all duplicate
            else:
                r -= 1


        return False









