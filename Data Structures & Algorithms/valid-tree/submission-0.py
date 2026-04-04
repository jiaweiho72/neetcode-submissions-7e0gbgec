class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Input: a list of UNDIRECTED edges (node, node)
        Output: Boolean if these make up a valid tree

        What is a valid tree?
        - connected
            - no isolated components
            - every node is reachable to other nodes
        - acyclic

        Idea: DFS
        conver to adjencency list first
        - Keep track of a visited set
        - connected: if final visited set == components set 
        - if cur node visited before -> cycle

        note: a node here is a simple int (0 to n - 1)
        """

        # Safety check: 
        # if len(edges) > (n - 1):
        #     return False


        # Initialise adjacency list
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # DFS
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            # visit neighbours
            neighbours = adj_list[node]
            for neighbour in neighbours:
                """
                Handle case of undirected. where currently you have
                a neighbour which is where you want to go next
                from the current node
                - if the 'next' neighbour is hte parent of the current
                node -> you are going back again
                - so need to keep track of the parent
                """
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node): # if any downstream is false
                    return False 
            return True

        # If there is a cycle
        if not dfs(0, -1):
            return False
        
        # check if all nodes are visited
        return len(visited) == n

            
        
        








