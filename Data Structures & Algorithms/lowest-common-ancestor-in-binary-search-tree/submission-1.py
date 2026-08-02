# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        19 July 2026
        - Given BST
        - return LCA node of two given nodes
            - lowest node that has both p and q as descendants.

        - BST so the moment p <= node <= q, it means it is the LCA alr
            - not possible to be furhter up as it means p and q are on the same side alr
            - not possible to be further down too as going down would go to either p side or q side
        - use the node value to determine to move righ or left
        
        """
        def dfs(node):
            if node.val > p.val and node.val > q.val: # larger than both -> look left
                return dfs(node.left)
            if node.val <  p.val and node.val < q.val: # smaller than both -> look right
                return dfs(node.right)
            else: # not larger than both and not smaller than both -> in between or equal to p and q
                return node

        return dfs(root)

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
            




