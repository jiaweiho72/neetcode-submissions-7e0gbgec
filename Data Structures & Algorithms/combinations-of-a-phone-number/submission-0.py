class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        dfs(i, cur_string) 

        """

        num_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        n = len(digits)
        def backtrack(index, cur_string): # index of the current output position
            if index >= n: # Done
                result.append(cur_string)
                return
            
            letters = num_to_char[digits[index]]
            for letter in letters:
                backtrack(index + 1, cur_string + letter)
        
        if digits:
            backtrack(0, "")   
        return result



        