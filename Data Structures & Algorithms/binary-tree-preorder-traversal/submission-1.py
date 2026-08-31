# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        - preorder node values
            - note while going down tree

        Time: O(n) visit every element
        Space: O(n) recursion stack and result list
        """

        preorder = []
        def dfs(node):
            if not node:
                return

            preorder.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return preorder