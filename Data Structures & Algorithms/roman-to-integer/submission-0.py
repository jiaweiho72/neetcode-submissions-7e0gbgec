class Solution:
    def romanToInt(self, s: str) -> int:
        """
        4 oct 2026
        - left to right, largest to smallest
        - xxx and next number is xy (4)
            - y is larger than x
        convert to integer


        idea
        - map symbol to number
        - just keep adding the numbers from left to right
            - handle case of IV
                - since I < V, it is 5 - 1. current add negative

        """
    
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n = len(s)
        result = 0
        for i in range(n):
            cur = roman_to_int[s[i]]
            if i + 1 < n:
                nxt = roman_to_int[s[i + 1]]
                if cur < nxt:
                    cur *= -1 # make it negative if it is the IV case
            result += cur

        return result











