class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        12 Jul 2026
        - return no of min no of minutes until no fresh orange. If impossible return -1

        solution
        - get the initial count of fresh oranges
        - get the positions of rotten oranges so that you can do the simulation from these
            - multi source BFS
        - simulate inplace the rotting of oranges
            - bfs from each rotten orange

        note if fresh count does not decrease for one round and it is not zero
            - means that it is stuck and won't change alr

        mistake:
        - combine the set is union not intersection
        - instead of rotten_set, use a queue for the BFS. That's all
            if set, for every iteration, you go through every single rotten orange again
            if BFS, you are visiting only the neighbours per iteration and the neighbours surround
                this node so this node does not need to be visited and naturally skipped
        
        Time: O(V)
        - As each orange is only processed once. not counted by the number of levels
            - yes main while loop is m + n
            - but inner, you have for loop which iterate per level
            - if you some all the inner for loop loops, everything = V
        - compared to set which is m*n * T where T is the no of rounds(mins) which is m + n
        Space: O(V) queue
        """
        from collections import deque
        m, n = len(grid), len(grid[0])

        # 1) initialise values
        fresh_count = 0
        queue = deque()
        for r in range(m):
            for c in range(n):
                cur = grid[r][c]
                if cur == 0: # ignore empty cell
                    continue 
                elif cur == 1: # fresh
                    fresh_count += 1
                elif cur == 2: # rotten
                    queue.append((r, c))
        
        # 2) Simulation of rotting
        rounds = 0
        while fresh_count and queue: # run until no fresh (must check for inifite case)
            level_size = len(queue)
            for i in range(level_size):
                r, c = queue.popleft()

                # visit all directions
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for y, x in directions:
                    new_r, new_c = r + y, c + x
                    if new_r in range(m) and new_c in range(n):
                        cur = grid[new_r][new_c]
                        if cur == 1:
                            queue.append((new_r, new_c))
                            fresh_count -= 1
                            grid[new_r][new_c] = 2

            rounds += 1
        
        # valid if fresh_count == 0 as all is rotten (after bfs is exhausted everywhere)
        return rounds if fresh_count == 0 else -1