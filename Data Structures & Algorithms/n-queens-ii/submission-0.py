class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        13 Oct 2026
        - same as n queens but return disintct solutions
            - previous was return all possible boards

        bruteforce -> same as I, but use a set

        ideal
        - is there a way to tell a path would be duplicate?
            if a 

        - for every row, you try every col

        no smart way about it
        - just n-queens but diff output
        - placing n queens in nxn square -> every row need one, every column need one constraint

        no need row set, as you are inserting one col at a time in a row
        - each row you need to choose one element to output (aka fill one col per row)
            - meaning each output position, has an isolated set of items to choose locally
            - like letter combindation telephone numbers
        """
        col_set = set()
        pos_diag_set = set() # i + j
        neg_diag_set = set() # i - j
        def dfs(row): # return count
            if row == n: # OOB -> can finish questions -> valid solution
                return 1
            
            distinct_count = 0
            for col in range(n):
                if (
                    col in col_set
                    or col + row in pos_diag_set
                    or col - row in neg_diag_set
                ): # skip if has a conflicting element
                    continue # path won't lead to a valid solution

                # try cell
                col_set.add(col)
                pos_diag_set.add(col + row)
                neg_diag_set.add(col - row)

                distinct_count += dfs(row + 1)

                col_set.remove(col)
                pos_diag_set.remove(col + row)
                neg_diag_set.remove(col - row)
            
            return distinct_count

        return dfs(0)

        