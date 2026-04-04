class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict(Counter(s))
        t_dict = dict(Counter(t))

        return s_dict == t_dict