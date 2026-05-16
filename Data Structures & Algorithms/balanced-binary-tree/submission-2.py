# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # """
        # dfs returning a bool
        # - at each point
        #     - get height of side tree and if balanced
        # """

        # # def dfs(node):
        # #     if not node: # node is none and reach end
        # #         return 0, True
        # #     left_height, left_is_balanced = dfs(node.left)
        # #     right_height, right_is_balanced = dfs(node.right)
        # #     is_balanced = abs(left_height - right_height) <= 1 and left_is_balanced and right_is_balanced

        # #     return max(left_height, right_height) + 1, is_balanced

        # # h, res = dfs(root)
        # # return res



        # """
        # 5 Apr 2026
        # - return boolean if is balanced
        # - balanced = left and right subtrees height difference <= 1

        # dfs 
        # - keep track of the height
        # - true until proven false
        # """


        # def dfs(node): # return height and bool
        #     if not node:
        #         return 0, True
        #     left_h, left_bool = dfs(node.left)
        #     right_h, right_bool = dfs(node.right)

        #     cur_bool = (
        #         abs(left_h - right_h) <= 1
        #         and left_bool
        #         and right_bool
        #     )

        #     return max(left_h, right_h) + 1, cur_bool

        # final_h, final_bool = dfs(root)
        # return final_bool


        """
        16 May
        height-balanced = every node the left and right differ by <= 1

        DFS and return the height of the tree (the max len) compare and return boolean too
        """

        def dfs(node) -> tuple[int, bool]: # height, is balanced 
            if not node: # reached the end
                return 0, True
            height_r, is_balanced_r = dfs(node.right)
            height_l, is_balanced_l = dfs(node.left)
            return max(height_r, height_l) + 1, (
                is_balanced_r
                and is_balanced_l
                and abs(height_r - height_l) <= 1
            )
        h, is_balanced = dfs(root)
        return is_balanced










