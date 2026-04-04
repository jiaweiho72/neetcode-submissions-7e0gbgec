class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        4 apr 2026
        notes
        - output: boolean
            - if s2 contains permutation of s1
            - aka permutation of s1 exists in s2
        - permutation -> count of characeters the same
        - fixed window size = len(s1)
        - lowercase letters

        mistakes
        - need one additional check again at the end or at the start


        30mins
        """
        from collections import Counter
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False

        # init
        s1_count = Counter(s1)
        s2_count = {}
        for i in range(l1):
            c = s2[i]
            s2_count[c] = s2_count.get(c, 0) + 1

        # main loop
        for r in range(l1, l2):
            cur = s2[r]
            l = r - l1
            print(l,r)
            print(s1_count, s2_count)
            if s1_count == s2_count:
                return True
            
            # movement right
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == 0:
                s2_count.pop(s2[l])
            s2_count[cur] = s2_count.get(cur, 0) + 1  

        # need extra check after as you last change is not checked  
        if s1_count == s2_count:
            return True
        return False # if nothing found






