class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        pass
        """
        4 Nov 2026
        - where to place new piece
            - must be in one of 8 directions connected to >= 1 consecutive OPPOSITE piece
            - followed immediately by a SAME piece
            - new piece must be endpoint of line
            - line must be >= 3 cells
            - place in cell [rMove, cMove]
                - colour given
        - return true if at least one line exists
        - must be straight line, immediate to the new piece is opp colour and end must be back to original colour

        idea
        - start search from new piece
            - dfs
            - form a path where immediately is opp colour and afterwards change back       
        """

        def helper(rMove, cMove, colour):
            if colour == "W":
                opp_colour = "B"
            else:
                opp_colour = "W"

            no_of_rows, no_of_cols = len(board), len(board[0])
            
            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]

            for dr, dc in directions:
                r, c = rMove + dr, cMove + dc
                # 1) check opp
                opp_count = 0
                while (
                    r in range(no_of_rows)
                    and c in range(no_of_cols)
                    and board[r][c] == opp_colour
                ): # valid
                    opp_count += 1
                    r += dr
                    c += dc
                if opp_count == 0: # no count -> invalid
                    continue

                # 2) same
                same_count = 0
                while (
                    r in range(no_of_rows)
                    and c in range(no_of_cols)
                    and board[r][c] == colour
                ):
                    same_count += 1
                    r += dr
                    c += dc
                if same_count != 0:
                    return True
            return False








        return helper(rMove, cMove, color)





