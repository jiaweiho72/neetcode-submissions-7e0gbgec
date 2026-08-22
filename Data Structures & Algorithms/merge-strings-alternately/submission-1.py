class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        merge alternately

        extension:
        if it's a list and need to be constant space
            - this needs the input with already extra space of size of other word at the back

        idea:
        - keep a list of the letters and then join at the end
        - better because concatenating a string each time creates a new string
        """

        merge_list = []
        n1, n2 = len(word1), len(word2)
        i1, i2 = 0, 0
        while i1 < n1 and i2 < n2:
            merge_list.append(word1[i1])
            merge_list.append(word2[i2])

            i1 += 1
            i2 += 1

        # actually don't need to check which to run, just run both, one will not append anything
        merge_list.append(word2[i2:])
        merge_list.append(word1[i1:])
        
        return ''.join(merge_list)





        


        