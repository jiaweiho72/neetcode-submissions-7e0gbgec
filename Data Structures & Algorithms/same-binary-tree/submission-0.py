# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        5 apr 2026
        - iterate through both at the same time and compare side by side
        """
        
        def dfs(p, q): # return bool
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False

            return (
                p.val == q.val
                and dfs(p.left, q.left)
                and dfs(p.right, q.right)
            )


        return dfs(p, q)