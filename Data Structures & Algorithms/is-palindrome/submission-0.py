class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        4 apr 2026
        1) two pointer
        2) reverse list and compare equality

        note: case insenstive and ignore non-alphanum
        """
        
        # clean
        cleaned_string = "".join(c.lower() for c in s if c.isalnum())

        string_reveresed = cleaned_string[::-1]
        return string_reveresed == cleaned_string