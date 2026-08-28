# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Binary search 
        - sorted number + searching for target + able to tell which side to search for target by comparison*
        """

        l, r = 0, n # not indexes but the actual number
        while l <= r: # == too as need to check single number too
            m = (l + r) // 2
            answer = guess(m)
            if answer == 0:
                return m
            elif answer == -1: # guess is higher -> m needs to be smaller
                r = m - 1
            else:
                l = m + 1
            
        return -1 # not possible

        