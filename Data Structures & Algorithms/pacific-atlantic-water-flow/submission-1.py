class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        7 Nov
        - Find all cells where water flows to both oceans
        - water flows from equal to lower cells

        idea
        - instead for from each m*n cells, and dfs to check m*n cells
            - start from the targets and just do from there
        
        do dfs from corner elements and only visit does where height is equal or taller neighbours
        mark each cell if can reach
        return intersection of boths sets of cells
        """

        rows, cols = len(heights), len(heights[0])
        visited = set()
        def dfs(row, col, visited):
            if (row, col) in visited:
                return
            visited.add((row, col))
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (
                    new_row in range(rows) 
                    and new_col in range(cols)
                    and (new_row, new_col) not in visited # alternative to using base case (edge case is the start of the dfs(0) not captured)
                    and heights[row][col] <= heights[new_row][new_col]
                ): # valid -> visit neighbour
                    dfs(new_row, new_col, visited)

        pacific_set = set()
        atlantic_set = set()
        for col in range(cols):
            dfs(0, col, pacific_set)
            dfs(rows - 1, col, atlantic_set)
        for row in range(rows): # one cell would be a duplicate work
            dfs(row, 0, pacific_set)
            dfs(row, cols - 1, atlantic_set)

        combined_set = pacific_set.intersection(atlantic_set)
        return [list(cell) for cell in combined_set]
        









        """
        12 July 2026

        - water flow to surrounding cells if these cells height is lower
        - return grid demarking for cells that can flow to both atlantic and pacific

        - concept
            - Sometimes it is more efficient to search from each cell
                eg. finding path to nearest treasure (there are multiple treasures so don't make sense to reverse as the first scan may not be accurate)
            - sometimes reverese is more efficient
                eg. this is fixed the starting point target, then you can from target, find if can reach the cells

        solution
        - dfs from each corner point touching the ocean. 
        - keep track in results set which cells can be reached
        - get the intersection between pacificn and atlantic set

        mistake:
        has to be less than or equal to to flow
        - reverse direction -> has to be more than or equal to prev
        """

        m, n = len(heights), len(heights[0])

        result = []
        def dfs(r, c, visited, prev_height):
            if r not in range(m) or c not in range(n) or (r, c) in visited: # invalid
                return
            cur = heights[r][c]
            if cur >= prev_height: # valid = water can flow
                visited.add((r, c))

                # visit all 4 directions
                dfs(r + 1, c, visited, cur)
                dfs(r - 1, c, visited, cur)
                dfs(r, c + 1, visited, cur)
                dfs(r, c - 1, visited, cur)
            else:
                # Did not add to visited: won't have infinite loop as it will just end and not visit anymore
                return

        pacific_set = set()
        atlantic_set = set()
        # 1) iterate through rows
        for r in range(m):
            # pacific
            dfs(r, 0, pacific_set, 0)
            # atlantic
            dfs(r, n - 1, atlantic_set, 0)

        # 2) iterate through cols
        for c in range(n):
            # pacific
            dfs(0, c, pacific_set, 0)
            # atlantic
            dfs(m - 1, c, atlantic_set, 0)

        result = pacific_set.intersection(atlantic_set)
        return [[pair[0], pair[1]] for pair in result]