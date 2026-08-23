class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        idea
        - same as palindrome but now if you find a non-match, give it chance

        Issue:
        edge case: "eceec"
        - if you just check if skipping the element will maintain palindrome in the next element, and select ONLY ONE of valid side, you will be wrong
        - in this case, ceec or ecee is a valid try
            - you need to check BOTH

        - thus, just try both
        """
        def is_palindrome(s):
            # constant space as compared to reveresing the string which is O(n)
            n = len(s)
            l, r = 0, n - 1
            while l <= r: # < or <= both works as if they are equal, it is automatically valid as it is the same element
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        n = len(s)
        l, r = 0, n - 1

        while l < r:
            if s[l] != s[r]:
                skip_left = s[l + 1:r + 1]
                skip_right = s[l:r]
                return is_palindrome(skip_left) or is_palindrome(skip_right)
            l, r = l + 1, r - 1

        # means already valid palindrome, never needed to delete
        return True 







            