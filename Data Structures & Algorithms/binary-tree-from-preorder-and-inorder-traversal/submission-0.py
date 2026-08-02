# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        How did I never tried this
        
        things i notice
        - preorder real dfs traversal -> main idea
            - first is the root
            - second is left
            - third could go left or right
        - inorder tells me order from left to right
            - tells me how much to going left until I find the ele equal to cur inorder ele
            - find equal -> bo back to parent -> go right

        - adding in preorder and using inorder to figure to put left or right
        - for loop iterate through preorder
            - if cur = 
        

        NEETCODE:
        - do with recursion:
            facts
            1) Preorder: first ele of preorder will ALWAYS be the root node to put
                ignoring the root, you can also split left and right subtree
                - no of elements on left | no of elements on the right
                - count determined from below
            2) Inorder: find the root's position in this list 
                -> then every value on the left is the left substree and same for right

            recursion - building one subtree at a time
            - root is the first element of preorder
            - let 'mid' be the index of the current root value in inorder list
                - this index partitions the left subtree on its left and right subtree to its right
            - split into two subtrees and set the root's left and right
                - make recursive call to build the left subtree
                    - preorder: ignoring the root, left subtree is size m
                        - left subtree is preorder[1: mid + 1] (+1 because +1 to ignore the root)
                        - right subtree is preorder[mid + 1:]
                    - inorder: 
                        - left: get everything from the left of mid excluding mid inorder[:mid]
                        - right: everything on the right of mid exlcuding mid inorder[mid + 1:]
            eg. 
            preorder = [3*, 9, | 20, 15, 7]
            inorder = [9, 3*, 15, 20, 7]

        Time:
        - list slicing is O(V)
        total: O(V^2)
        
        Space:
        O(V^2)

        """

        def helper(preorder, inorder):
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0]) # get index

            root.left = helper(preorder[1:mid + 1], inorder[:mid])
            root.right = helper(preorder[mid + 1:], inorder[mid + 1:])
            return root

        return helper(preorder, inorder)