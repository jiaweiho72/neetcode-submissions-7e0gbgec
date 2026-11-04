class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        5 Nov 2026
        - similar to partitioning the string but now you can skip letters
            - instead of returning boolean if can, return some other optimal thing
            - word break is about dfs(i) where i is if you can form contiguous words from i onwards
        - return min no of extra chars left over and still break up

        instead of trying every letter one by one and checking if in dict, for each dict word, find in string

        method 1:
        for each letter in string, try form extend word with the char or start a new word with it
        - keep track of the characters used
        - if can't find a valid word, it would just keep extending the word string
        O(2^n)
        - n is 50
        - if cache, would have multiple args
            - plus, you would go down many paths where there just isn't any valid dict word

        method 2:
        for every dict word, try to see if it exists in the string
        - dict length 50
        - straight away can try to use valid dict words rather than trying every letter one by one and hoping it is a dict word
        - dfs(i), can minimise the arguments

        dfs(i) -> return the min no of extra characters left if you try to form a word at i
            - at i, try to form starting a word
            - the return will encompass case where you start a word from i and case when you skip char at i

            if no more characters left, the 

            for each word in dict
                try to form a word starting with it
            try not forming a word to and skip to next index 
        """


        from functools import cache
        n = len(s)

        @cache
        def dfs(i):
            if i == n:
                return 0

            min_chars = n - i # start with max (assume all can't be used)
            cur_str = s[i:]
            for word in dictionary:
                if cur_str.startswith(word):
                    # simulate word is used so not in char count, get count from index after this word
                    min_chars = min(min_chars, dfs(i + len(word)))
            min_chars = min(min_chars, dfs(i + 1) + 1) # skip this i and try form word starting from next index (must add to unused words)
            return min_chars

        return dfs(0)



