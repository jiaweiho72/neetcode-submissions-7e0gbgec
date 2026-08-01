class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Question
        - given two strings s and t, return SHORTEST substring of s
            - where every character in t (including dups) is in substring
        
        Assumption
        - correct output is always unique

        Bruteforce
        - get the alphabet count of t
        - go through every possible substring of s and corresponding alphabet count
        O(len(s) ^ 2)
        constraint len(s) <= 10^3

        Optimisation
        - get the alphabet count of t
        - subtring of s get the alphabet count too
            - move right pointer until every character is present
            - move left pointer pointer until first missing character
        Time: O(n)

        tip: comparing dicts especially when you have to delete and compare is some stuff to manage
        mistake: you can't just compare dict==dict here because the count won't be exact
            - you can have additional characters or additional counts of character
            - alternative is to have wrapper function to compare dict every time to compare
                only characters of t. but that would have a nested O(len(t))
            - use a having count
                - each iteration you already compare for that specific character

        tip: s[i:n] is O(n) time complexity, so hold the index first
        - counting along the way in the pass rather than each time comparing every char count is more efficient


        mistakes
        - while left < right should be <=
            s="ab"
            t="a"
            - without equal, it did not check the case for single index left == right
        - need should be len(t_count)

        Time: let m be len(t), n be len(s)
        - outer for loop len(n):
            - inner while loop in total every outer loop = m so not counted as inner
        O(m + n)

        Space: dictionaries O(no of unique characters) not alphabets also
        """
        from collections import Counter
        # 1) Init the count dict of t (array also can)
        t_count = dict(Counter(t))

        # 2) Main sliding window (two pointer)
        min_length = float("infinity")
        min_substring = [-1, -1] # start and end index 
        s_count = {}
        having, need = 0, len(t_count)
        left = 0

        for right in range(len(s)):
            cur_char = s[right]
            s_count[cur_char] = s_count.get(cur_char, 0) + 1
            
            # matched a new count: not >= because you only want to update once not everytime
            if cur_char in t_count and s_count[cur_char] == t_count[cur_char]:
                having += 1

            while having == need: # while at least valid. don't need to check lef <= right tbh as not possible. need to be == too as single
                # If here, still valid as 'having == need'
                cur_length = right - left + 1
                if cur_length < min_length : # question say won't have == tie
                    min_length = cur_length
                    min_substring = [left, right]
                
                s_count[s[left]] -= 1
                
                # check if lost a valid character -> next round having != need
                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]:
                    having -= 1

                left += 1
        l, r = min_substring
        return s[l: r + 1] if min_length != float("infinity") else ""

            














        