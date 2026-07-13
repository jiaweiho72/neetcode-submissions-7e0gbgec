class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        13 July 2026
        union find or just DFS
        - return no of connected components

        solution with DFS
        - for every node, do dfs and visited all that's current connected in the path
        - for subsequents, don't visit the visited

        note: undirected
        """
        # 1) convert to adj set first
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)


        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            # visit neighbours
            neighbours = adj_list[node]
            for neighbour in neighbours:
                dfs(neighbour)

        connected_count = 0
        for i in range(n):
            if i not in visited:
                connected_count += 1
                dfs(i)

        return connected_count        
        
        
        
        
        
        
        
        
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












