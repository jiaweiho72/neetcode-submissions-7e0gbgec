# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        5 apr 2026
        - invert
        """

        def dfs(node):
            if not node:
                return
            left = node.left
            right = node.right

            node.left = right
            node.right = left

            dfs(left)
            dfs(right)

        dfs(root)

        return root

            
