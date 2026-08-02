class Solution:
    def trap(self, height: List[int]) -> int:
        """
        30/09/25

        Idea:
        - For every index point, determine how much blocks of water it can stack on top
        - Logic:
            - Get the max heights of the left and right of current point
            - The minimum of these will be the height of the water. 
                - No matter the order of things in between
                - even if there are smaller blocks in between the water height will still
                rise to be the min of the left and right max
            - Use this height and minus the current height to get the water height
                - note that the current height may be a new max height and the left or right
                may be smaller. This case, the no water can be stored

        - Hack to save space
            - you can just use two pointers for left/right max heights
            - move the pointer that has smaller height
                - cus you are using the l/r max heights to find the MIN of the two
                - so the smaller one will ALWAYS be the min cus other right values will only be larger

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