class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        if element is 0, set entire row and column to 0 inplace
        - if a cell was inplace set to 0, don't count this

        idea
        - extra memory space to keep track of which needs to be set to 0

        optimised no space idea
        - just use another value like 'x' to demarcate that the row/column is to be zeroed
            - just need to set on one of the column value to tell 
                -> for convenience and easy searching when setting, just set the first col/row
                - this still prevents conflict as if you are iterating from the first col/row so it changing the value won't affect the subsequent visits
                    - like you would have already visited it (confirm visited alr)
        - just need something that conflicts and confuses with 0

        Mistake:
        1) in the second pass, you must first avoid the first row first (overlap)
            - or else whole first row is all 0 and subsequently you will zero everything
            - then lastly need to recheck the row again

        2) the 0, 0 column is tricky as there is overlap
            - you need a way to differentiate if the value is for row and the col to be zeroed
            - so default store for the row + a separate boolean to store the col
        """

        m = len(matrix)
        n = len(matrix[0])
        first_col_zero = False

        # initial checking
        for r in range(m):
            for c in range(n):
                cur = matrix[r][c]
                if cur == 0:
                    if c == 0:
                        first_col_zero = True
                        continue

                    matrix[r][0] = matrix[0][c] = 0
        
        # Zeroing rows
        for r in range(1, m):
            cur = matrix[r][0]
            if cur == 0: # to zero the whole row
                for c in range(n):
                    matrix[r][c] = 0
        
        # Zeroing columns
        for c in range(1, n):
            cur = matrix[0][c]
            if cur == 0:
                for r in range(m):
                    matrix[r][c] = 0

        # zero only first row
        if matrix[0][0] == 0:
            for c in range(n):
                matrix[0][c] = 0

        # zero only first col
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0
        