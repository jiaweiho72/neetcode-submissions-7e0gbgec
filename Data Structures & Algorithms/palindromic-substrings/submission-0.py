class Solution:
    def countSubstrings(self, s: str) -> int:
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


