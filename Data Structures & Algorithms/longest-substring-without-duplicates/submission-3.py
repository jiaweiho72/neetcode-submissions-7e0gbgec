class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        4 apr 2026
        notes
        - longest length of contiguous string without duplicate

        sliding window two pointer
        - keep track of elements with a dict as you need to keep track of last occurrence index
        - iterate through -> if got duplicate
            - left pointer move to the last point of occurrence

        - right pointer just continues iterating at constant rate
            - won't have conditional movement like the left pointer

        mistake
        - you moved the left pointer but you need to clear all the other
        elements from there to current
        """

        max_length = 0
        n = len(s)

        l, r = 0, n - 1
        char_set = set()
        for r in range(n):
            cur = s[r]

            # Handle duplicate
            # remove until the last occurrence is also removed
            while cur in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Check max after handling duplicate
            max_length = max(max_length, r - l + 1)
            # update last occurrence no matter what
            char_set.add(cur)
            
        return max_length



