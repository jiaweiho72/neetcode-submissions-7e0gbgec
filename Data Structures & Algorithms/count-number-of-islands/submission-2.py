class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        12 July 2026
        - return number of connected components

        solution
        - dfs/bfs on every cell and mark the cells along the way in visited set
            - just need to see all the cells that this cell can visit
            - both dfs/bfs works
        - if not in visited, and is land, it is a new island
            - in this case, we reuse the visited set globally
                - don't need to mark the water as visited as it will alr be ignored


        mistake:
        - must still check if visited as you are searching all directions and there is this case
            - example at row r, you dfs r + 1 but at r + 1, you would search -1 which is r again
            - this leads to infinitely searching the same cell


        Time:
        - even though there is an m x n loop calling dfs inside. dfs does not run fully for all O(m * n)
            - inside dfs, the total nodes you visit every iteration is one part of V
                - because you check visited and don't revisit
                - so sum the visits every iteratoin you get V
                - it is not the case where every loop you visit V nodes, only one part of V
                - so time is O(+V) and not * V
                - also for every node visited, it visits it's neighbours too
                    - like even if it points to an already visited node, it will still go there and run the 'is visited' check
                    - so +E
            so the internal sum from dfs is O(V + E)
        - Final: O(V)
            - O(m * n + V) = O(2(m * n)) because V = m * n

        Space:
        - O(V) visited set
        - O(V) recursion stack
        - Final: O(2V)
        """

        m = len(grid)
        n = len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if r not in range(m) or c not in range(n):
                return
            cur = grid[r][c]
            if cur == "0" or (r, c) in visited: # water, no more path
                return
            
            # reach here means that is "1" and valid connection -> add to visited
            visited.add((r, c))

            # visit 4 directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return

        no_of_islands = 0
        for r in range(m):
            for c in range(n):
                cur = grid[r][c]
                if cur == "1" and (r, c) not in visited: # start a new land
                    no_of_islands += 1
                    dfs(r, c)
            
        return no_of_islands














        # BFS to find islands
        visited = set()

        m, n = len(grid), len(grid[0])

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            while queue:
                r, c = queue.popleft()
                if (r, c) not in visited:
                    visited.add((r, c))
                    # Visit neighbours
                    # directions -> up down left right
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for dr, dc in directions:
                        new_r = r + dr
                        new_c = c + dc                        
                        if ((new_r) in range(m) and
                            (new_c) in range(n) and
                            (new_r, new_c) not in visited
                            ):
                            if grid[new_r][new_c] == "1":
                                queue.append((new_r, new_c))
                            # else: # is 0
                            #     visited.add((new_r, new_c))
                            """
                            Reason why you don't visit "0" is
                            so that you have a place to stop, 
                            else you will visit the whole map

                            though you could set it to visited
                            so it won't visit it again.
                            """


        count = 0
        for i in range(m): # For each row
            for j in range(n): # For each columns
                cur = grid[i][j]
                
                if (i, j) not in visited and cur == "1": # Ignore if visited or not a land
                    bfs(i, j)
                    count += 1
        return count
        
                