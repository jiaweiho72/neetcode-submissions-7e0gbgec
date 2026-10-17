class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        17 Oct 2026
        - return true if word present in grid

        idea
        - outer loop try every start letter
        - try path that is valid
        - keep a visited loop to prevent moving back to previously used in current path
        

        the backtracking is the visited set which in this case is not global visited
        but it is the path visited. Basically it is a path items
        - so backtrack
        """

        rows, cols = len(board), len(board[0])
        n = len(word)
        visit_path = set()

        def dfs(row, col, i): # i is the current letter position in word, return True
            if i == n: # found valid 
                return True
            if (
                row not in range(rows) 
                or col not in range(cols)
                or (row, col) in visit_path
                or board[row][col] != word[i]
            ):
                return False
            visit_path.add((row, col))
            
            # go 4 directions
            bool_res = (
                dfs(row + 1, col, i + 1)
                or dfs(row - 1, col, i + 1)
                or dfs(row, col + 1, i + 1)
                or dfs(row, col - 1, i + 1)
            )
            visit_path.remove((row, col))

            return bool_res

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False











        """
        Hais back in the bi nance
        - run backtrack on every cell to find the word - to save you could run only if cell start with the first letter
            - traverse in every direction
            - check if within border

        - case: infinite recursion where you keep going back to the same place
            - use visited set based on (r,c)
            - works if you back track, removing from visited and maintaining it's 
            original state
                - in backtracking questions, it is important to leave things in it's original state as not everything is ran at once and it does dfs for the recursion tree. So you do one part first then go back to the parent and do other parts, you have to return it in a clean state or it will leak to other parts. Like recursion it will just keep going but you have to manually change back to the original state

        m = number of rows
        n = number of columns
        L = length of word
        Time: O(mn⋅4L)
        Space: O(L)

        why not DP
        - the state space is too large. even for dfs(r, c, i)
            - it depends on what nodes you have already visited
            - suppose you visited x and you call a cached value of dfs(r, c, i)
                - but this cached value of dfs(r, c, i) call may have came from a path that visited x
        """

        m = len(board)
        n = len(board[0])
        word_len = len(word)
        visited = set() # (r, c)

        # returns a boolean
        def backtracking(r, c, i):
            if (
                r not in range(m) or c not in range(n) or # Check if r, c in bounds
                board[r][c] != word[i] or # Check if can't form word
                (r, c) in visited # Check not alr visited
            ):
                return False
            
            # If reach end of word -> FOUND
            if i >= word_len - 1:
                return True

            visited.add((r, c))
            # Go all 4 directions
            bool_res = (
                backtracking(r + 1, c, i + 1) or
                backtracking(r - 1, c, i + 1) or
                backtracking(r, c + 1, i + 1) or
                backtracking(r, c - 1, i + 1)
            )
            visited.remove((r, c)) # if you don't remove, other steps that have not used this will still have it in visited
            return bool_res

        # main loop
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if backtracking(r, c, 0):
                        print(r, c)
                        return True
        return False