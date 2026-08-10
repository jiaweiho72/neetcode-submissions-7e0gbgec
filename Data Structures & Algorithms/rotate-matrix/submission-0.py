class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # r = c, c = r

        # m = len(matrix)
        # n = len(matrix[0]) # Same as m as it is N X N
        # top, bottom = 0, m - 1
        # left, right = 0, n - 1

        # # left, right = 0, len(matrix) - 1
        

        # while left < right: # for each full border cycle
        #     for i in range(right - left): # each sub cycle = n - 1 times
        #         print(i)
        #         top, bottom = left, right
        #         # Swap clockwise - don't change the l,r,t,b pointers
        #         # Letting all first row be the starting point
        #         top_left = matrix[top][left + i] # Store temp to be used later
        #         matrix[top][left + i] = matrix[bottom - i][left]
        #         matrix[bottom - i][left] = matrix[bottom][right - i] 
        #         matrix[bottom][right - i] = matrix[top + i][right]
        #         matrix[top + i][right] = top_left

        #     # Shrink border inside
        #     # top += 1
        #     # bottom -= 1
        #     left += 1
        #     right -= 1

        """
        2nd try
        - Two pointer
            - Iterate for each spiral layer -> while l < r
        - in each iteration:
            - for each element:
                - rotate it's friends in the other 3 sides
        """
        n = len(matrix)
        l, r = 0, n - 1

        # For each spiral layer -> l/r corresponds to up down also as square
        while l < r:
            no_of_ele = r - l + 1 - 1 # corners are repeated
            t, b = l, r
            for i in range(no_of_ele):
                # Start swap at top left clockwise -> but traverse anticlockwise
                top_left = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l] # top left
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = top_left
            l += 1
            r -= 1
        