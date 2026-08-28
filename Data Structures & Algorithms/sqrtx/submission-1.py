class Solution:
    def mySqrt(self, x: int) -> int:
        """
        28 Aug 2026
        - given positive int x, return square root rounded down (no internal functions)

        square root: need to search for the number that multiplied together int*int = x

        range of value = (0,x) # non-negative
        - make range smaller?
            x = 1; (0,1) -> could be up to x
            x = 4; 2
            x = 9; 3
            x = 16; 4
            x = 25; 5
        - can be seen that answer range is much smaller than x
        - BUT -> with binary search, it DOES that, it cuts search by half everytime alr
            - you don't need to do it the first time

        * round down
        """

        l, r = 0, x

        while l <= r: # need to check single digit too 
            m = (l + r) // 2
            squared = m * m
            if squared == x: # found answer
                return m
            elif squared < x: # need to increase value
                l = m + 1
            else:
                r = m - 1

        # not possible to find squareroot but round down
        return l - 1



        
        