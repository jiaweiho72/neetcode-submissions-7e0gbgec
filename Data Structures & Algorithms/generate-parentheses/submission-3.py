class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        3 Aug
        Pattern
        - return all permutation -> backtracking
        - well formed 
            - at the end -> must be closed -> equal number of open and close at the end
            - at any point of time, you can never have more close than open

        backtracking
        - args : closed/open count
        - return -> empty
            # - boolean if valid parentheses
        - main recursion
            - base case: open == close count == n (no of pairs)
            - try open and try close. There is no option to not choose (no skipping)
            invalid cases
                - open is less than closed
                - open is more than n (n pairs so should have less than n open)
                - closed is more than n (first case already handled)

        * use a stack as it is more efficient 

        Time: O(2^2n * n)
        - every recursion two options. 2^2n = 4^n
        - * n for the base leaf node join (negligible)

        Space: O(n)
        - recursion stack
        - result is each string max = 2n
            and there are 4^n leaf nodes
            - so 4^n * n
        """
        result = []
        cur_stack = []

        def dfs(open_count, closed_count):
            # base case
            if open_count == closed_count == n: # valid
                result.append(''.join(cur_stack))
                return
            if (
                open_count < closed_count
                or open_count > n
            ):
                return 
            
            # 1) Try add an open
            cur_stack.append("(")
            dfs(open_count + 1, closed_count)
            cur_stack.pop()

            # 2) Try add a close
            cur_stack.append(")")
            dfs(open_count, closed_count + 1)
            cur_stack.pop()

        dfs(0, 0)
        return result








        """
        9 Apr 2026
        Pattern
        - return all permutation -> backtracking
        - well formed 
            - at the end -> must be closed -> equal number of open and close at the end
            - at any point of time, you can never have more close than open

        backtracking
        - global variable
            - current string
        - params
            - closed/open count
        - return 
            - empty return
            # - boolean if valid parentheses

        every step there are two choices -> open or close
        - no skipping
        """

        cur_str = ""
        result = []
        final_length = n * 2
        def backtracking(closed_count):
            nonlocal cur_str
            cur_len = len(cur_str)
            open_count = cur_len - closed_count

            if cur_len == final_length: # out of bounds -> check
                if closed_count == open_count:
                    result.append(cur_str)

                return 
            
            # invalid cases with early return 
            if (
                closed_count > open_count
                or closed_count > n
                or open_count > n
            ):
                return
            
            cur_str += "("
            backtracking(closed_count)

            cur_str = cur_str[:-1]
            cur_str += ")"
            backtracking(closed_count + 1)
            cur_str = cur_str[:-1]

        backtracking(0)
        return result


