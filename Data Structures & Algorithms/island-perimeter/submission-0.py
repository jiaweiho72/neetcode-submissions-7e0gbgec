class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        One connected component
        - dfs through the component
        - perimeter of island is the the sum of sides
            - each cell starts off with 4 sides. every adjacent elemtent minus 1
        - do dfs on down and right to avoid double=counting

        must do dfs from every point as you don't know which point is connected

        - iterate for each row, each col
            - if water cell, skip
            - assumme default perimeter is 4
        - iterate right and down
            - recheck previous and left if adjacent
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: # water: ignore
                    continue

                perimeter += 4 # assume 4 (no adjacent elements)
                if r > 0 and grid[r - 1][c] == 1: # check top
                    perimeter = perimeter - 1 - 1 # minus for this cell and minus for the above cell
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter = perimeter - 1 - 1

        return perimeter





