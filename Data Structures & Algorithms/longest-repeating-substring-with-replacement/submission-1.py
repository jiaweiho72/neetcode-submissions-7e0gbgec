class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        notes
        - input: uppercase letters
        - chooese up to k chars in the string and replace them
        - output: after performing at most k replacements
            return length of longest substring with ONLY ONE distinct character
        
        ideas
        - to count how many replacements to get distinct
            - get the character with max count
                - dictionary
            - get the complement of that max count (would be the min replacements needed)
        - movement
            - r is static
            - l moves to maintain the max count < k
        """

        n = len(s)
        max_length = 0
        l = 0
        count_dict = {}
        
        for r in range(n):
            c = s[r]
            count_dict[c] = count_dict.get(c, 0) + 1 # increment
            max_count = max(count_dict.values())
            cur_length = r - l + 1

            if cur_length - max_count <= k: # valid
                max_length = max(max_length, cur_length)
            else: # need to reduce the substring size so that you need one less replacement
                count_dict[s[l]] -= 1
                l += 1

        return max_length
            






