# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        14 Jul 2025
        - set left and right border range
        - each dfs return bool

        - local decision
            - intuitive is check the max_left < cur < min_right
            - BUT NO, do in reverse
                - for each node, it must be within a narrowing boundary based on ancestors
                basically at parent: looking for now at the right side first
                - everything on the right must be larger than it, so on this right side, it's new left side boundary is now parent
                - this narrows with every depth downards
                for the root, the boundaries are inifite as there are no ancestors

        * concept: the immediate parent will always be the one being the narrowest closing down the range
        """

        def dfs(node, l, r):
            if not node:
                return True
            return (
                l < node.val < r and
                dfs(node.right, node.val, r) and
                dfs(node.left, l, node.val)
            )
        return dfs(root, float('-inf'), float('inf'))