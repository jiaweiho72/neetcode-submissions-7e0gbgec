class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

