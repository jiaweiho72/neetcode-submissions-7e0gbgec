class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        """

        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[m] < nums[l]: # right region
                # decide when to shift left or right
                # if need smaller go left, if target bigger than the right, go left
                if nums[m] > target or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                
                    
            
            else: # left region
                if nums[m] < target or target < nums[l]: # when to shift right
                    l = m + 1
                else:
                    r = m - 1

                    
        return -1