class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
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


