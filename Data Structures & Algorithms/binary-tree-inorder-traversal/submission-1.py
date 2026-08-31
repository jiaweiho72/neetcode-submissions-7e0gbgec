# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Inorder
        - return inorder traversal the values

        Time: O(n) # visit every node once
        Space: O(n) # result list and recursion stack
        """

        inorder_result = []

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            inorder_result.append(node.val)
            dfs(node.right)
            

        dfs(root)

        return inorder_result
