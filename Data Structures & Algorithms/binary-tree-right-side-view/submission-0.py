# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        20 Jul 2026
        - return right side value
        
        solution
        - BFS
            - level order
            - track the rightmost element, constantly update the rightmost
                as the right most may be none and you need the next non-null rightmost


        mistake: 
        'if level_rightmost' i used the value to check if None, but value = 0 also counted in
        """

        from collections import deque
        def bfs(root):
            q = deque([root])
            result = []

            while q:
                level_size = len(q)
                level_rightmost_node = None
                for i in range(level_size):
                    cur = q.popleft()
                    if not cur: # ignore if none
                        continue
                    
                    level_rightmost_node = cur
                    # visit neighbours (must visit left before right)
                    q.append(cur.left)
                    q.append(cur.right)
                
                if level_rightmost_node:
                    result.append(level_rightmost_node.val)
                    
            return result
        
        return bfs(root)