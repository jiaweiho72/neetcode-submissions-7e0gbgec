# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        5 Apr
        Level order
        - BFS
            - queue (deque)
            - usually every iteration you handle one by one
                - not a level every iteration

            - but since you need to return per level
                - easier to do per level than to keep track of level everytime
                - if handle by level each time queue state is per level
        return in list(int)
        """
        from collections import deque
        
        # handle empty case
        if not root:
            return []
        queue = deque()
        queue.append(root)
        
        result = []

        while queue:
            level_size = len(queue)
            cur_level = []
            print(queue)
            for i in range(level_size):
                node = queue.popleft()
                cur_level.append(node.val)

                # visit neighbours ( will be added to the queue but not yet processed)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(cur_level)
        return result








