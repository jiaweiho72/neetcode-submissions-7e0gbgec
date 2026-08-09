class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Valid parenthesis but wildcard * can be (, ) or empty
        
        intial idea: wrong
        - normal stack check and if invalid - see if there is * to use
        - problem: it is not linear and you still have to try multiple options at each step
            - like you may set to replace the * with ( immediately but maybe it would have been valid
                if you waited a bit more
        note: can't pop empty list
        """






        """
        Bruteforce: DFS O(3^n)
        - normal valid parenthesis backtracking but if wildcard, do 3 actions
        DP memoisation: O(n^3)

        typical invalid cases:
        1) you can never at any point have more close than open
        2) at the end, you still have open that are not closed


        Greedy: O(n) time; O(1) space
        - keep track of a left_min and left_max
        - concept: 
            - valid if diff between no of open and no of closed = 0
            - wildcard makes it possible a variation
            - use the two values as the 'range'
        - left_min -> all use close
            - left_min is the minimum possible number of unmatched
        - left_max -> all use open
        - in between this range -> use mix of * etc

        key: how to handle cases of more open than close
        """
        n = len(s)
        left_min, left_max = 0, 0
        for i in range(n):
            if s[i] == "(":
                left_min += 1
                left_max += 1
            elif s[i] == ")":
                left_min -= 1
                left_max -= 1
            else: # wildcard *
                left_min -= 1 # close
                left_max += 1 # open
            
            if left_max < 0: # invalid case: more close than open (even after using * for open)
                return False
            """
            since the above alr checks for too many close
            - below happens when we use too many * as close
                - reset to zero when negative -> 'change' prev * to be empty or open
            """
            if left_min < 0: 
                left_min = 0
        return left_min == 0 # if > 0 -> more open than close 
            