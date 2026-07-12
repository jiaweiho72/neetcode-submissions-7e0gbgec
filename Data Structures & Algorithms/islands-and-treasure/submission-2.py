class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        """
        12 jul 2026
        - modify in place
            - fill land cell with distance to nearest treasure
            - remain inf if can't reach treasure

        - unweighted -> BFS until find a treaure
            - thought of reverse -> from treasure find land
                - but this may not be the shortest, so still go from land
        """
        from collections import deque
        m, n = len(grid), len(grid[0])
        
        def bfs(r, c):
            visited = set()
            q = deque([(r, c)])
            distance = 0
            while q:
                # length of current level
                level_length = len(q)
                for i in range(level_length):
                    r, c = q.popleft()
                    if (r, c) in visited:
                        continue
                    if r not in range(m) or c not in range(n):
                        continue
                    visited.add((r, c))

                    cur = grid[r][c]
                    if cur == -1: # water ignore and don't continue path
                        continue
                    if cur == 0: # found the first treasure
                        return distance
                    else: # inf or inplace int = land
                        # visit all neighbours
                        q.append((r + 1, c))
                        q.append((r - 1, c))
                        q.append((r, c + 1))
                        q.append((r, c - 1))
                distance += 1

            return 0 # return 0 if can't find treasure

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2147483647:
                    shortest_dist = bfs(r, c)
                    if shortest_dist: # only update if distance != 0 meaning can reach treasure
                        grid[r][c] = shortest_dist

        return






        """
        Input: 2D grid
        Output: void return but the change the grid in place
        - for each land cell -> update distance to nearest 0
        - cannot traverse through -1

        Bruteforce Idea
        - BFS from each land cell to find shortest path
        issue: O(V+E) * size of matrix

        Optimised 
        - reverse idea
        - start from treasure chests
            - Do BFS with ALL chests as starting point
            - BFS all together at once and immediately update the land
                - it's as if you are in the second step of normal BFS
        """
        # from collections import deque
        # treasures = [] # list of (r,c)
        # m = len(grid)
        # n = len(grid[0])

        # # Find cell indexes of all treasures
        # for r in range(m):
        #     for c in range(n):
        #         cur = grid[r][c]
        #         if cur == 0:
        #             treasures.append((r, c))

        # # BFS
        # q = deque(treasures)
        # visited = set() # set of cells
        # cur_level = 0

        # while q:
        #     level_size = len(q)
        #     print("level" + str(level_size))
        #     for i in range(level_size):
        #         r, c = q.popleft()
        #         if (
        #             (r,c) in visited
        #             or r not in range(m)
        #             or c not in range(n)
        #             or grid[r][c] == -1 # skip if water
        #         ):
        #             continue
        #         visited.add((r,c))
        #         if grid[r][c] == 2147483647:
        #             grid[r][c] = cur_level

        #         # visit neighbours - go all directions
        #         q.append((r, c + 1))
        #         q.append((r, c - 1))
        #         q.append((r + 1, c))
        #         q.append((r - 1, c))
        #     cur_level += 1

        # return



        








