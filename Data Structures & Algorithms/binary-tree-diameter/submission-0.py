# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        5 apr 2026
        - same as max depth but you add the left and right together
        """

        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter

            if not node:
                return 0
            
            left_h, right_h = dfs(node.left), dfs(node.right)
            max_diameter = max(max_diameter, (left_h + right_h + 1))
            return max(left_h, right_h) + 1
        
        dfs(root)

        return max_diameter - 1 # no of edges not no of nodes



