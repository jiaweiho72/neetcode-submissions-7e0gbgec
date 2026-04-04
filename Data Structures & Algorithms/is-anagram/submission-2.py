class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_dict = dict(Counter(s))
        # t_dict = dict(Counter(t))

        # return s_dict == t_dict

        """
        30 Mar 26
        - compare counts
        """
        from collections import Counter
        s_dict = dict(Counter(s))
        t_dict = dict(Counter(t))
        return s_dict == t_dict

