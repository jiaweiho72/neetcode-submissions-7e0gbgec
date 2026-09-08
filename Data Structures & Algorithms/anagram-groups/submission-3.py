class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        9 Sep 2026
        - group anagrams together

        idea
        - for each word, need to get the count of each alphabet
        - group in dict those strs where the 26 letter alpha count is the same
            - dict as you can have mapping from unique count to the strs with this count
            - fast to be able to know where to put for a specific count - O(1) lookup
        - as dict keys must be immutable 
            - first use a list: index is the alpha ordinal, value is the count
                - this is better than a letter:count dict cause dict you again need to 
                    make it immutable
            -> convert list to tuple for immutability
        - at the end, convert back to lists

        11:33
        Time: O(n + c) where n is no of strs and c is no of characters total
        Space: O(n + c) dict
        """
        from collections import defaultdict
        n = len(strs)
        NO_OF_ALPHA = 26
        result = defaultdict(list)
        for i in range(n):
            cur_str = strs[i]
            alpha_count = [0] * NO_OF_ALPHA
            for char in cur_str:
                index = ord(char) - ord('a')
                alpha_count[index] += 1
            
            tuple_alpha_count = tuple(alpha_count)
            # result[tuple_alpha_count] = result.get(tuple_alpha_count, []) # init if not exist
            result[tuple_alpha_count].append(cur_str)
        
        return [val for key, val in result.items()]










        """
        30 Mar 26

        - output: group anagrams together in sublist

        - group words by a dict key (dict count of each letter)
            - use a list where the index is the alphabet to save one dimension
                - else it is another nested dict
            - dict key must be unique and immutable -> convert list to dict
        """
        from collections import Counter

        n = len(strs)
        result = {}

        for i in range(n):
            cur = strs[i]
            cur_count = [0] * 26
            for c in cur:
                index = ord(c) - ord('a')
                cur_count[index] += 1
            cur_count = tuple(cur_count)
            result[cur_count] = result.get(cur_count, [])
            result[cur_count].append(cur)
            


        return [ i for i in result.values()]

