class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        3 Apr 2026
        - Check horizontal
        - Check vertical
        - Check per 3x3 box


        - for checking duplicates -> set for quick O(1) check if element exits
            - lists take O(n)
            - don't need to check other constraints as number is guaranteed 1-9 or '.'
                - ignore '.' in checking duplicate

        - output boolean if valid\
        """
        # m and n is fixed at 3x3
        m = len(board)
        n = len(board[0])

        # checking horizontal per row
        for r in range(m):
            cur_row = set()
            for c in range(n):
                cur = board[r][c] # get is O(1)
                if cur == '.': # ignore
                    continue
                else:
                    if cur in cur_row:
                        return False # duplicate found
                    cur_row.add(cur)

        # checking vertical per column
        for c in range(n):
            cur_col = set()
            for r in range(m):
                cur = board[r][c]
                if cur == '.': # ignore
                    continue
                else:
                    if cur in cur_col:
                        return False # duplicate found
                    cur_col.add(cur)
        
        # checking boxes step of 3
        for i in range(0, m, 3):
            for j in range(0, n, 3):
                cur_box = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        cur = board[r][c]
                        print(cur)
                        print(cur_box)
                        if cur == '.': # ignore
                            continue
                        else:
                            if cur in cur_box:
                                return False # duplicate found
                            cur_box.add(cur)


        # if nothing found -> valid
        return True




