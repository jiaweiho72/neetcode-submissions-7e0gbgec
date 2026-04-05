# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        5 Apr 2026
        - return depth -> no of nodes along longest path

        - get the max of the left and the max of right side
        """

        # max_depth = 0
        # def dfs(node):
        #     nonlocal max_depth
        #     if not node:
        #         return 0

        #     left_h, right_h = dfs(node.left), dfs(node.right)
        #     max_depth = max(max_depth, (left_h + right_h + 1))

        #     return max(left_h, right_h) + 1 # add the current node

        # dfs(root)
        # return max_depth

        def dfs(node):
            if not node:
                return 0
                
            left_h, right_h = dfs(node.left), dfs(node.right)
            return max(left_h, right_h) + 1

        max_depth = dfs(root)
        return max_depth






