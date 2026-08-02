# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        19 Jul 2026
        - return kth smallest value (1 indexed)

        idea
        - BST: smallest value on the left
        - dfs
            - left < parent < right
            - increment like this post order
        """
        result = None
        order = 0
        def dfs(node):
            nonlocal result
            nonlocal order
            if not node: # reached leaf node
                return

            # visit left first before right
            dfs(node.left) # goes left all the way first
            order += 1
            if order == k:
                result = node.val
                return # early return and stop traversing
            
            dfs(node.right)
        
        dfs(root)
        return result