class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Output: no of connected components

        Idea: similar to number of islands
        - keep track of a visited set
        - dfs on every node and skip if visited
            - each new dfs adds to the count
        """

        # 1) Create adjency list
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # 2) DFS
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            # Visit neighbours
            neighbours = adj_list[node]
            for neighbour in neighbours:
                dfs(neighbour)
            return
            
        # 3) Count
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count












