class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        4 apr 2026
        - return boolean -> if target exists

        idea
        - binary search the right row first
        - then binary searcht that row

        8mins
        """

        m = len(matrix)
        n = len(matrix[0])

        # search for row
        t, b = 0, m - 1
        row = 0
        while t <= b:
            m = (t + b) // 2
            if target < matrix[m][0]: # need to look up at smaller rows 
                b = m - 1
            elif target > matrix[m][-1]: # need to look down at larger rows
                t = m + 1
            else: # found the row where target is in between
                row = m
                break
        
        # search in the row
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False # if not found





                