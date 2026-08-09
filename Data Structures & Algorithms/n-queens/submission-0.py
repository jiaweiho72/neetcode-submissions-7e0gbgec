class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Question:
        - Return a list of all possible n-queens board
        - Queens travel vertically, horizontally and diagonally (any amount)
        - Ensure no Queens clash AKA in the same col, row, diagonal

        Idea: Brute-force backtracking
        1) Maintain 3 sets
            a) col -> Keep track of which column is used so that you don't add a queen in 
            the same col
            b) posDiag which similarly to ensure queens are not in the same diagonal
            - Denoted by (r + c) as this is constant for every r,c pair along the diagonal
            c) negDiag denoted by (r - c)
        2) Just backtracking by the row and check for each col where it can put the queen


        note: you could pass the sets as arguments but there is no need as it is a global thing reference
        """

        result = []
        col_set = set()
        pos_diag_set = set() # r + c /
        neg_diag_set = set() # r - c \
        board = [["."] * n for _ in range(n)] # Initialise board

        # Going through each row so there is no clash
        def backtracking(row):
            if row == n: # reached the end
                copy = [''.join(row) for row in board]
                result.append(copy)
                return
            
            for col in range(n):
                # If current row, col is invalid as there is a conflicting queen
                if col in col_set or (row + col) in pos_diag_set or (row - col) in neg_diag_set:
                    continue # This goes to the next iteration of the loop
                
                # Try add in row, col
                col_set.add(col)
                pos_diag_set.add(row + col)
                neg_diag_set.add(row - col)
                board[row][col] = "Q"

                backtracking(row + 1)

                # Backtrack and try another column
                col_set.remove(col)
                pos_diag_set.remove(row + col)
                neg_diag_set.remove(row - col)
                board[row][col] = "."
        
        backtracking(0)
        return result