class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        24 Jul 2026
        - Bruteforce is from every land, we find the path to treasure. Then have an outer loop to do BFS on every land
            - However, unlike other island questions where it is about finding connectivity, 
                this is more about find best path -> so you would need to refresh the visited set every BFS
                as previously visited node may be part of optimal path in next BFS
                - this will lead to O(V^2)

        Optimal
        - reverse, search from treasure to land
            - at first it seems non-optimal current BFS from treasure would not be aware of distance against other treasures
            - thus to resolve this, do multi BFS
        - start BFS at every treasure and move level by level. The first leve lands from the treasure has the shortest path to treasure
            - so basically start the queue with all the treasures inside
            - then BFS from them like normal

        still need to keep track of no of levels so must check level
        """
        from collections import deque
        m, n = len(grid), len(grid[0])

        # 1) Get the the treasures
        treasure_list = []
        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                if cur == 0:
                    treasure_list.append((i, j))

        def bfs(): # no input as the start is not a point, but every point in treasure_list
            queue = deque(treasure_list)
            visited = set()
            cur_distance = 0
            
            while queue:
                level_size = len(queue)
                for i in range(level_size):
                    r, c  = queue.popleft()
                    if r not in range(m) or c not in range(n): # out of bounds
                        continue

                    # no point revisiting points that are not land (-1, 0) meaning no valid path or land that was already visited and updated with shortest path
                    if (r, c) in visited:
                        continue
                    
                    visited.add((r, c))
                    cur = grid[r][c]

                    if cur == -1:
                        continue

                    # removed the below, because it would never visit the initial treasure this way
                    # if cur == 0:
                    #     continue
                    if cur == 2147483647:
                        grid[r][c] = cur_distance
                    
                    # visit neighbours
                    queue.append((r + 1, c))
                    queue.append((r - 1, c))
                    queue.append((r, c + 1))
                    queue.append((r, c - 1))
                    
                # after going through one level -> update the distance
                cur_distance += 1
        bfs()
        return 
                    
                








        """
        *** NOT OPTIMAL ***
        12 jul 2026
        - modify in place
            - fill land cell with distance to nearest treasure
            - remain inf if can't reach treasure

        - unweighted -> BFS until find a treaure
            - thought of reverse -> from treasure find land
                - but this may not be the shortest, so still go from land



        Time:
        - Main loop O(V). Inner call to BFS = O(V + E)
            - HOWEVER, it is NOT using a global visited set, each BFS use a new set
                - every V processing it will visit Ev neighbours
                    - all neighbours visited will sum to ~E
                so V + E
            so main loop * O(V+E) = O(V^2 + V*E)
        

        Space
        - visited set, recursive stack, queue
        - O(V)
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



        








