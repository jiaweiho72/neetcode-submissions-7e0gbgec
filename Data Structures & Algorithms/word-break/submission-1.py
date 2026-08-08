class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        25 Jul 2026

        - return true if s can be segmented into sequence of one or more dict words
            - cannot miss any letters
        - allowed to reuse dictionary words
        
        idea
        - bruteforce search 
        - go through every char in s and build a substring
            - check if in the dictionary
                - if inside:
                    continue with a new empty substring
                    - edge case 'pet' 'pets'
                        - found alr but should still have one more path to continue trying more letters
                - else:
                    continue searching

                needs at least one to be true
        False until proven true
        Time O(n^2) where n is the length of s
            - s <= 300 -> O(n^2)
        Space O(n)

        30 mins
        """

        from functools import cache
        n = len(s)
        
        @cache
        def dfs(i, cur_string):
            # base case
            if i == n: # reached end, it must form a full word
                if cur_string in wordDict:
                    return True
                else:
                    return False

            cur_string += s[i]
            valid_break = False
            if cur_string in wordDict: # found a match
                # start finding a new word
                if dfs(i + 1, ''):
                    valid_break = True
                
            # OR continue extending current word regardless if matched or not
            if dfs(i + 1, cur_string):
                valid_break = True
            
            return valid_break

        return dfs(0, '')