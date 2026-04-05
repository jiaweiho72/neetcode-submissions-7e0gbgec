# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        6 apr 2026
        BST
        LCA - lowest node such that both p and q are descendants
        - ancestor can be descendant of itself
        return LCA node

        idea
        - LCA is the first point where p and one side and q is another side
        - all other cases, p and q are on the same side



        mistake
        no need dfs
        bst you can find the position of p/q as it is ordered


        """

        cur = root

        while cur:
            # decision to move

            # move left is cur is more than both pq
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                # found the LCA - when pq are no longer on the same side
                return cur
            




