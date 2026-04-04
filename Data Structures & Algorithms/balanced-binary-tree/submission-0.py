# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        dfs returning a bool
        - at each point
            - get height of side tree and if balanced
        """

        def dfs(node):
            if not node: # node is none and reach end
                return 0, True
            left_height, left_is_balanced = dfs(node.left)
            right_height, right_is_balanced = dfs(node.right)
            is_balanced = abs(left_height - right_height) <= 1 and left_is_balanced and right_is_balanced

            return max(left_height, right_height) + 1, is_balanced

        h, res = dfs(root)
        return res





