class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        input - List of List of triplets
        output - boolean on whether possible to obtain the target

        brainstorm:
        - you need the max of every ele to be the target
        - if it is the correct number, it must be the larger one
            - if you found the correct num, you must find a one with smaller num

        - brute force O(n^2)
            - for every triplet, check every other triplet

        - iterate through triplet
            - if any number is the target AND the rest are below the other targets:
                -> valid -> that number is completed

        main idea:
        - a triplet is invalid if any number is larger than target
        - for valid triplets, check if each index of the target exists in any valid triplets

        - to keep track of which index of target has been found -> use set as no duplicates
        - it is a bit complicated to just use one loop
            - because if you find matching, you would update 
                but later on there may be element making it invalid.
                hard to backtrack and still know the index that was found
            - better to check for validness first before checking target
        """

        n = len(triplets)
        res = set()
        for i in range(n):
            t = triplets[i]
            # If any is larger than target -> Invalid -> skip
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for j in range(3):
                if t[j] == target[j]:
                    res.add(j)

        return len(res) == 3
        




