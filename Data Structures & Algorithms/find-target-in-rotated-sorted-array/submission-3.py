class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1 Nov 2026
        if left region
        - determine when to go right
            target is less than the the leftmost
            target is more than mid
        - when to go left
            target is less than mid and target is more than leftmost

        return index
        """

        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[m] > nums[r]: # left region
                if target < nums[m] and target >= nums[l]: # go left
                    r = m - 1
                else:
                    l = m + 1
                    
            else: # right region
                if target > nums[m] and target <= nums[r]: # go right
                    l = m + 1
                else:
                    r = m - 1
        return -1

        """
        4 apr 2026
        - return index of target found in nums or -1 if not found
        - all unique elements

        - right region
            - if m less than target -=> need larger
                - if target more than the right side, need to search leftwards
                - if smaller, search rightwards
            - if m more than target -> need smaller
                - just need to go leftwards

        30mins

        don't need to check if unrotated as the normal conditions would cover such cases
        - from you target vs middle check
        - getting min does not do that check
        """

        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[m] < nums[l]: # right region
                # when to go left: If target less than mid or target is on the left sorted side
                if nums[m] > target or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                
            else: # left region
                # these below checks help to clear cases where unrotated
                if nums[m] < target or target < nums[l]: # when to shift right
                    l = m + 1
                else:
                    r = m - 1

                    
        return -1