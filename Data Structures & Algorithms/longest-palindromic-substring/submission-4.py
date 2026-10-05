class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        return longest substring that is palindrome (the actual substring)

        - bruteforce, O(n^2) - for each, element, go through 

        idea
        - for each element
            - expand outwards
                - even and odd case handling

        """
        

        n = len(s)
        max_substring = ""

        for i in range(n):
            # even
            l = i
            r = i + 1
            while l in range(n) and r in range(n) and s[l] == s[r]:
                cur_substring = s[l:r + 1]
                if len(cur_substring) > len(max_substring):
                    max_substring = cur_substring
                l -= 1
                r += 1
            
            # odd
            r = l = i
            while l in range(n) and r in range(n) and s[l] == s[r]:
                cur_substring = s[l:r + 1]
                if len(cur_substring) > len(max_substring):
                    max_substring = cur_substring
                l -= 1
                r += 1
            
        return max_substring
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        25 july 2026
        - return LONGEST palindromic substring

        DP
        - iterate for each element
            - from center, fan out
                - take note of odd and even case
                - two pointer

        Questions
        - is there guaranteed solution
        - is answer unique

        mistake: don't need to form the string, can use the index

        Time: O(n ^ 2)
        - Outer n loop
            - inner search could be n extendable palindromes
                - if max length -> operation slice string n
                    - but it happens rarely
        
        Space: O(n)
        - n string output
        """
        # helper


        n = len(s)
        max_length = 0
        longest_palindrome = ''

        # n is not updated or assigned and just called -> no need for nonlocal
        def check_palindrome(l, r): # returns the longest palindrome found
            nonlocal max_length
            nonlocal longest_palindrome

            while l in range(n) and r in range(n) and s[l] == s[r]:
                cur_length =  r - l + 1
                if cur_length > max_length:
                    max_length = cur_length
                    longest_palindrome = s[l : r + 1]

                # fan outwards
                l -= 1
                r += 1
            return

        for i in range(n):
            # even case
            l, r = i, i + 1
            check_palindrome(l, r)

            # odd cases
            l, r = i, i
            check_palindrome(l, r) # to prevent add both same left and right

        return longest_palindrome