class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        """
        reverse with O(1) memory
        - note string slicing is O(n) -> creates new string everytime

        idea
        - two pointer swap
        """

        n = len(s)
        l, r, = 0, n - 1

        while l < r:
            s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1