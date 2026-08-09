class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        30 Jun 2026
        notes
        - each part must not have repeating letters

        idea:
        - a hashmap of letter:last seen index
        - iterate from first letter and keep changing the end index according to the hashmap

        return: list of integers representing size of each parts
        """

        # First iteration - Initialisation
        n = len(s)
        last_seen = {} # get the first occurence index from the back
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c not in last_seen:
                last_seen[c] = i

        # Second iteration
        result = []
        cur_start, cur_end = 0, 0
        for i in range(n):
            if i > cur_end: # start a new partition
                # add to result
                result.append(cur_end - cur_start + 1)
                cur_start = i
            c = s[i]
            cur_end = max(cur_end, last_seen[c])

        # add the last partition
        result.append(cur_end - cur_start + 1)
        return result