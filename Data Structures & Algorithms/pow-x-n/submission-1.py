class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Rakuten Question

        edge cases:
        - negative (-2) -> inverse fraction
        - fraction (1/2)
        """

        # result = 1
        # for i in range(abs(n)):
        #     result *= x
        
        # if n < 0:
        #     result = 1 / result
        
        # return result

        """
        Above is O(n) but need to do an O(logn) as there is a lot of repeated calculations

        Idea:
        - Recursive and breakdown the operation n by half everytime
            - note: handle when n is odd and even
        - Handle the negativity of the exponent only at the end
        """

        def helper(x, n):
            if n == 0:
                return 1
            result = helper(x, n // 2) # Get the floor division
            result *= result
            # Handle odd or even
            return result if n % 2 == 0 else result * x

        result = helper(x, abs(n))
        return 1 / result if n < 0 else result



        