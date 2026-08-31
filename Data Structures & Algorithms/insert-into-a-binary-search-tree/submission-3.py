# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        - insert into BST 
            - need to maintain order
        - guaranteed new node not in original BST
        - return the root node

        search from the node
        - if more than cur -> go right
        - else go left

        obeservation
        - never a case you need to reorganise nodes
            - cause you will just extend downwards left or right
            - and the new value guaranteed not to exist
        - the first null is where it belongs

        if you keep track of parent, alot of things to keep track, like which side of the parent to add
        also need to keep track of dummy pointer

        - edge case:
            empty list, no parent to add to -> manually add a new TreeNode

        Time: 
        - WRONG: O(logn) as you only explore one side of each branch. It is not 1/2 n but it is half the
        search space at every step
        - above only true if BST is balanced and not like a single linked list
            - if single linked list, could be up to O(n)
            - so it depends on the heigth -> final O(h)

        Space: O(1)
        """
        if not root:
            root = TreeNode(val)
            return root

        def dfs(node):
            if not node:
                # the first and only time it reaches here
                return TreeNode(val)
            
            if val > node.val:
                node.right = dfs(node.right)
            elif val < node.val:
                node.left = dfs(node.left)
            else: # impossible
                pass
            
            return node
        
        dfs(root)
        return root