class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        9 Aug 2026
        Optimal not 2D

        instead of searching if word in wordDict, search every word in wordDict and see if can form word
        - instead of going index by index and search, jump index for each word in dict

        
        n = len(s)
        D = len(wordDict)
        L = maximum word length in wordDict

        Time: O(n * D * L)
        - dfs called max n times
            - each dfs search through every word in dict D
                - each word has string slicing of L


        Space:
        - cache n
        - recursive stack is still n even though dfs called > n
            - because if cached, won't hit the stack
        """

        from functools import cache
        
        n = len(s)

        @cache
        def dfs(i):
            if i == n: # reached the end -> no previous false return -> valid
                return True

            for word in wordDict:
                # check if substring from i:i + len(w) is word
                if (
                    (i + len(word)) <= n # actually is len(w) -1 as i is included
                    and s[i: i + len(word)] == word
                ):
                    if dfs(i + len(word)):
                        return True
            # if reach here, no valid word found
            return False
        return dfs(0)








        
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


        Time O(n² · L?)
        n = len(s)
        D = len(wordDict)
        L = maximum word length in wordDict
            - s <= 300 -> O(n^2)
        
        Space O(n^2)
        - n^2 cached states i,cur_string

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