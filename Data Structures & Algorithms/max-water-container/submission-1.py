class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        4 apr 2026
        - Input: int array of heights
        - output: return max volume of water

        Solution
        - two pointer
        - move the side smaller next
            - because it has alr found the max volume for this height and distance
            - volume = min_height * distance
        
        5mins
        """

        max_vol = 0
        n = len(heights)
        l, r = 0, n - 1
        while l <= r:
            # check current volume
            cur_volume = min(heights[l], heights[r]) * (r - l)
            max_vol = max(max_vol, cur_volume)

            # update the next search
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        
        return max_vol







