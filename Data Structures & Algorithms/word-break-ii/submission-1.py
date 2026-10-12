class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        13 Oct 2026
        - add space in string s to form valid sentences with words in the dict
        - return all sentences -> backtracking
            if count, maybe can DP
        - same word can be reused multiple times

        idea
        - check each time if valid word in dict
            - valid or not, still try to extend the word
            - OR try to form a new word
                - add existing word to sentence, then continue to new word
        - if all s used up -> valid output

        no DP as you need every combination


        in order, no skipping, so your choice is the only the next element. No multi for loop option
        optimisation: use list for sentence rather than string
        - string slicing is O(n)
        - list just join at the end
        
        23 mins
        Time: O(2 ^ n) * n 
        - 2 choices -> n levels
            - each root answer does O(n) join
        Space: O(n), n levels

        Optimisations
        - wordDict is a list -> convert to dict
        - can early prune if the size of word is larger than the max possible size
        """


        result = []
        cur_sentence = []
        cur_word = ""
        n = len(s)

        # Optimisation 1)
        wordDict = set(wordDict)

        def dfs(i): # i = index of input
            nonlocal cur_word

            if i == n: # OOB but the previous was valid -> correct answer
                result.append(" ".join(cur_sentence))
                return

            original_word = cur_word
            cur_word += s[i]

            # 1) Don't use current word -> continue building word
            if i != n - 1: # if it is the last character -> cannot skip current -> force the below check
                dfs(i + 1)

            # 2) Use current word (only if valid)
            if cur_word in wordDict:
                tmp = cur_word

                cur_sentence.append(cur_word)
                cur_word = ""
                dfs(i + 1)
                cur_sentence.pop()

            cur_word = original_word
            
        dfs(0)
        return result








