"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        12 July 2026
        - return a DEEP copy

        solution
        - similar to the deep copy of the random linked list
            - traverse and map all the current and new nodes first
            - traverse again to do the adjacency mapping


        Important
        - as this graphs may have cycles and you are visiting all directions at every node (may revisit revers)
            - unlike trees, base case can't rely on not node
            -> always use visited sets

        - undirected


        Time:
        1) One pass DFS O(V + E)
            you visit every node AND PROCESS it O(V)
            - per node, you visit all neighbours and it will call dfs even if visited before. Only in the dfs call it will 
            do O(1) operation to check if visited
                - you don't visit all edges per node so it is not V * E
                - but the some of all the visits will add up to E
                    E1 + E2 + E3 = E where Ei is the no of outedges from node i
        2) Second pass the same
        - final O(2(V+E)) = O(V+E)
        note: unlike matrix, E != V

        Space:
        - visited, recursion stack, old_to_new mapping (V)
        - final O(3V)
        """
        old_to_new = {}

        
        # 1) map old to new nodes
        visited = set()
        def dfs(node):
            if node in visited or not node: # visited or reached end
                return
            visited.add(node)

            old_to_new[node] = Node(node.val)
            for neighbour in node.neighbors:
                dfs(neighbour)
        
        dfs(node)

        # 2) map the edge connections now
        visited = set()
        def dfs_edge(node):
            if node in visited or not node:
                return
            visited.add(node)
            for neighbour in node.neighbors:
                old_to_new[node].neighbors.append(old_to_new[neighbour])
                dfs_edge(neighbour)

        dfs_edge(node)

        return old_to_new[node] if old_to_new else node