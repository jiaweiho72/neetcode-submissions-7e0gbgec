class Solution:
    def frequencySort(self, s: str) -> str:
        """
        5 Nov 2026
        Bucket Sort
        - usually counts use dict. but dict has no order
        - sorting after would take nlogn
        
        - what if use a fixed size list where index is the count
            - because you are sorting by the count and not sorting by the element
                - you could make a list where index is the value. but hard to make the list beforehand
                    without knowing the range of possible values
            - the limit bound is the range of count (n items) rather than the range of possible values

        answer: highest to lowest
        note: you must return the char the number of times it has like if there are 3e, you need eee
        
        time: O(n) * 3 where n is size of s
        space: O(n)
        """
        from collections import Counter

        counts = dict(Counter(s))
        n = len(s)
        freq_list = [[] for _ in range(n + 1)] # can have up 0 to n count

        for char, count in counts.items():
            freq_list[count].append(char)

        result = ""
        for i in range(n + 1 - 1, -1, -1): # highest first
            char_list = freq_list[i]
            for char in char_list:
                result += char * i

        return result
