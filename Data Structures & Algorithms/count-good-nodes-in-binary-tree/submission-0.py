# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        29 jun 2026
        - good: path from root to X, X is hte largest number (equal ok)
        - return no of good nodes

        idea
        - DFS and keep track in order the current max
        - track a global count

        inorder you put as arguments and pass it downwards
        postorder you return the value and use it upwards
        """
        def dfs(node, cur_max):
            if not node: # reached end
                return 0
            
            no_of_good = 0
            if cur_max <= node.val: # current is a good node
                no_of_good += 1
                cur_max = node.val
            return no_of_good + dfs(node.left, cur_max) + dfs(node.right, cur_max)

        return dfs(root, root.val)