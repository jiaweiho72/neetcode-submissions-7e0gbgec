class Solution:
    def trap(self, height: List[int]) -> int:
        """
        30/09/25

        Idea:
        - For every index point, determine how much blocks of water it can stack on top
        - Logic:
            l, r = 0, n - 1
            go through one block at a time and calculate it's height
            - Get the max heights of the left pointer and right pointer
            - The minimum of these will be the side we will process as current
                - if curent max left side is smaller
                    - it means that the cur block on the right of max_left is guranteed this height
                        - because it doesn't matter if there are smaller blocks in between. It is smaller than the max right so worst case, the water will flow till it
                    - note that current height may be >= max_left_height. 
                        - This case, no water can be stored as every on the left is smaller so won't hold up
                        - height = 0 and you update the max_left height too
                    update the max_left
                - else
                    same thing, but process the right side

        note: the left and right boundaries won't store water
        """

        n = len(height)
        l, r = 0, n - 1
        max_left, max_right = height[l], height[r]
        amount = 0

        while l < r:
            if height[l] <= height[r]: # move the left pointer
                l += 1
                max_left = max(max_left, height[l])
                amount += max_left - height[l] # max_left is the min of both max_left and max_right

            else: # right is smaller
                r -= 1
                max_right = max(max_right, height[r])
                amount += max_right - height[r]

        return amount