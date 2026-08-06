class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        - tree = undirected graph + no cycles
        - given an edge list
        - return an edge that can be removed so that resulting graph is a tree (return the one that occurs LAST in input)
        - basically find the edge that removes the cycle

        idea
        1) Normal dfs cycle detection
            - record the path in the cycle
            - at the end, iterate through the input to find the last edge

        2) union find
        - join individual nodes together by iterating throug the edge list
        - if when adding an edge, you realise both src and dest have the same parent -> same component -> problem edge
        """

        # 1) init the parent list (each node point to itself as a parent). Let index be the node
        n = len(edges) # no of nodes = edges + 1 - 1
        parent = [i for i in range(n + 1)] # +1 because 1-indexed

        def find(node):
            # search until find the root parent
            if parent[node] == node: # reached the root
                return node

            # compress on the way
            parent[node] = find(parent[node])
            return parent[node]

        size = [0] * (n + 1)
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2: # problem edge
                return False

            # Reach here -> continue to union the two components

            # optimised by size (build flatter graph) -> the shorter component should be added as the child
            if size[p1] < size[p2]:
                parent[p1] = p2
                size[p2] += size[p1]
            else:
                parent[p2] = p1
                size[p1] += size[p2]
            # parent[p1] = p2
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return []