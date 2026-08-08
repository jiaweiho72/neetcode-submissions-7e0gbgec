class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        25 July 2026
        - return NUMBER of palindromic substrings

        same as longest palindromic substrings
        - instead of max, get the count, slightly easier
        
        DP
        for each char
            - look at even and look at odd to count
        Tips
        - better to not build the string as it is edgy to do the odd case as you add duplicate at the same index i

        Time O(n^2)
        Space O(1)
        """

        n = len(s)
        palindrome_count = 0

        # helper function to search as it repeats between even and odd
        def check_palindrome(l, r):
            nonlocal palindrome_count

            while l in range(n) and r in range(n) and s[l] == s[r]:
                # if reach here, found a valid expansion of the palindrome
                palindrome_count += 1

                # continue fan out
                l -= 1
                r += 1
            
            return

        for i in range(n):
            # even
            l, r = i, i + 1
            check_palindrome(l, r)

            # odd case
            l, r = i, i
            check_palindrome(l, r)
        
        return palindrome_count

        """
        9 apr 2026
        - return no of substrings within string s that are palindromes
        
        idea
        - start from the middle and branch out
            - different case for even and odd
        """

        n = len(s)
        count = 0
        for i in range(n):
            cur = s[i]

            # For finding odd palindromes
            l, r = i, i

            while (
                r in range(n)
                and l in range(n)
                and s[l] == s[r]
            ):
                count += 1
                l -= 1
                r += 1


            # For finding even palindromes
            l, r = i, i + 1 # next and don't go back
            while (
                r in range(n)
                and l in range(n)
                and s[l] == s[r]
            ):
                count += 1
                l -= 1
                r += 1
        return count


