class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        4 apr 2026
        - return index of target else -1
        binary search is always on sorted array
        """

        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target: # too large -> need to smaller value -> look left
                r = m - 1
            else:
                l = m + 1
        
        return -1