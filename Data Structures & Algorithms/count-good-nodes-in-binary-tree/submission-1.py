# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        6 Sep 2026
        - good node: root to x contains no nodes greater than x
        - return no of good nodes

        - dfs and keep track the current path max
        - keep a sum of the good nodes count

        dfs(node, cur_max) # returns the count of good
        - need to keep track of cur_max like this

        node can be negative
        """

        def dfs(node, cur_max):
            if not node:
                return 0

            cur_count = 0
            if cur_max <= node.val: # cur greater
                cur_count += 1
                cur_max = node.val
            
            return cur_count + dfs(node.left, cur_max) + dfs(node.right, cur_max)

        return dfs(root, float('-inf'))
        
            














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