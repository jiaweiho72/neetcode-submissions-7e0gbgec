"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        10 Sep 2026
        - break a grid into smaller grid with topleft, topright,bottomleft, bottomright
        - break until you reach a grid where all elements are the same -> root node
            - set isLeaf = True and val to the value of the elements
        - each level you parse, is one level on the tree
            split into 4 every level

        - are there examples with no leaf nodes? maybe

        idea
        - it is costly to go through every element but ok log4n
            - each cell is the sum from top left to it
        - each recursion, split into 4 sections. if one section
            - base case, already 4 elements
            - check if full square all the same, if not -> split

        NOTE: question says n is a factor of 2 so even. And is a square
        """

        n = rows = cols = len(grid)
        RANDOM_VALUE = 0

        # 1) prefix sum
        prefix_sum = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            row_sum = 0
            for col in range(cols):
                row_sum += grid[row][col]
                if row != 0: # if not the first row
                    prefix_sum[row][col] += prefix_sum[row - 1][col] # add previous above row's sum
                prefix_sum[row][col] += row_sum

        # 2) main dfs
        def dfs(row_start, col_start, size): # this are the corners
            # base leaf node cases
            if size == 0: 
                return None

            # a) main
            row_end = row_start + size - 1
            col_end = col_start + size - 1
            actual_sum = prefix_sum[row_end][col_end]

            # b) minus top
            row_top = row_end - size
            col_top = col_end
            if row_top in range(n):
                actual_sum -= prefix_sum[row_top][col_top]

            # c) minus left
            row_left = row_end
            col_left = col_end - size
            if col_left in range(n):
                actual_sum -= prefix_sum[row_left][col_left]

            # d) add overlap
            row_overlap = row_end - size
            col_overlap = col_end - size
            if row_overlap in range(n) and col_overlap in range(n):
                actual_sum += prefix_sum[row_overlap][col_overlap]

            # main check
            if actual_sum == 0: # all zeros or all ones -> root node
                return Node(val = 0, isLeaf = True)
            elif actual_sum == (size * size):
                return Node(val = 1, isLeaf = True)

            # Else, split into 4 parts
            cur_node = Node(val = RANDOM_VALUE, isLeaf = False) # non-leaf can be any value
            cur_node.topLeft = dfs(row_start, col_start, size//2)
            cur_node.topRight = dfs(row_start, col_start + size//2, size//2)
            cur_node.bottomLeft = dfs(row_start + size//2, col_start, size//2)
            cur_node.bottomRight = dfs(row_start + size//2, col_start + size//2, size//2)

            return cur_node

        return dfs(0, 0, n)
            

















