class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        12 Jul 2026
        - return max area of an island

        solution
        - same this a no of islands, but now keep track of the max area
            - dfs: keep track of the no of cells in connection



        Time:
        - O(m * n) main nested for loop + O(V) as visited set will make you visit AND PROCESS each node max constant time + O(E) as it will visit each
        neighbour and still run check if visited. so O(2(m * n) + E). can't ignore E but E = V in matrix 
        - FINAL: O(m * n)
        
        Space:
        - visited set and recursion stack
        - O(V)
        """
        
        m = len(grid)
        n = len(grid[0])

        visited = set()
        max_area = 0
        def dfs(r, c): # return the area
            if r not in range(m) or c not in range(n) or (r, c) in visited: # reached the end or alr visited
                return 0
                
            cur = grid[r][c]
            if cur == 0: # invalid water
                return 0
            
            visited.add((r, c)) # reach here means valid -> visit it
            
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + 1

        for r in range(m):
            for c in range(n):
                cur = grid[r][c]
                if cur == 1 and (r, c) not in visited: # start of new island
                    print(r, c)
                    area = dfs(r, c)
                    max_area = max(max_area, area)

        return max_area