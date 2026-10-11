class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        12 Oct retry
        
        - fixed size output: len(matchsticks)
        - unlike combinations where you skip previous elements if your for loop is not the first index
            (aka only the first index still have access to the rest of the elements)
            - this case, you need to use all elements. the above works as you still search the
            case of using in the first index. But you can cut out the extra skipping paths
            - thus, just directly use the current element at i and don't need you try every possible
            value of i to n. There is no need to skip elements
        - this is unlike permutations too, eventhough both cannot skip elements
            - yes current element you use, but you have other options to use for this position to create a permutation
            - this question does not matter the order you added the elements
        - thus when need to use every element, cannot skip it.
            - permutation will not skip, it tries every element and marks it as used in the path
            - this level, it 
        - just loop over the directions


        Ok i got it
        - compare with combination: yes the order does not matter, so you should not have a [1,2] and [2,1] being processed
            - using the visited set would cause this repeated calculation. This does not affect answer but is extra work
            - the normal combination for loop is flawed too, as it would be skipping elements
                - it works for combination because combination is meant to not use all elements. Using all elements means
                it is xCx = 1 and only has one combination

        - compare with permutation: it does not need order but it is similar in terms that it needs to use
        all elements
            - for permutations to use all elements, you try every unused element at one output position
            - for matchsticks, since no permutation and you can't skip elements
                - use current element as per normal
                - no need to have a for loop that creates branches in the current level
                    - this means it is skipping elements at i (don't choose i)

            - no need permutation, no need revisit previous elements before current -> no need visited set
                - like basic combination with a slight twist
                - how it handles the use all part
                    - only mark visited on one element each time
                    - it basically the samething
                        - every dfs level, it is adding one element to output until it uses everything and output is full
                        - just that every level, permutations, need to branch out, because need to try different element
                        at each output position
                        - combination use all, is just using one branch from it
            - cannot skip elements, must use all and is combination -> no for loop, just use current index
                - for a combination question where result must use all
                    - xCx = 1 and thus, you each dfs is just adding one element -> one combination only
                    - for loop is just creating conditions that are invalid (skipping elements)
            

        for combination, yes you append every iteration and the reason is because the for loop is unlike
        choose don't choose where there is explicit don't choose. The for loop choose at least one element
        and there is no skip. So yeah, but it does skip elements, by moving further down the for loop but
        it won't not select any element in a level

        optimisations
        - sort in reverse order -> quickly error break when filling large ones rather than fill small slowly one by one
        
        example [1,3,4,2,2,4]
        let each of 4 branch means the sides
        
                        1           1           1           1
                    2 2 2 2     2 2 2 2     2 2 2 2     2 2 2 2
        
                                                            [0,0,0,0]
                    [1,0,0,0]                           [0,1,0,0]       [0,0,1,0]       [0,0,0,1]
        [3,0,0,0]   [1,2,0,0]   [1,0,2,0]
                    
        """

        n = len(matchsticks)
        # Optimisation 1) 
        matchsticks.sort(reverse=True)
        total_sum = sum(matchsticks)
        if total_sum % 4 != 0: # not dividable by 4
            return False
        side_length = total_sum // 4
        sides = [0] * 4

        def dfs(i): # i is the current matchstick to use. Return bool
            # can't depend on i == n to determine if valid as it may hit it but the sum on one side is whack. need both
            if i == n and len(set(sides)) == 1: # reached end (all items used) and all sides equal
                return True

            # no for loop for choosing input, but for loop for choosing each output direction
            cur = matchsticks[i]
            seen = set() # add seen side length. If adding j creates a side length that alr exists -> repeated work
            for j in range(4):
                # Optimisation 2
                """
                in the sides, if one side is equal to another side. Adding j in this either side
                makes no diff and is repeated work. Ignoring other sides. The loop is iterating
                each side of the SAME sides list. so this just check for this current sides list,
                which sides are equal
                """
                if sides[j] in seen:
                    continue
                seen.add(sides[j])

                if sides[j] + cur > side_length: # invalid size
                    continue
                sides[j] += cur
                if dfs(i + 1):
                    return True
                sides[j] -= cur
            
            return False # if did not early break true

        return dfs(0)
            











        """
        12 Sep 2026
        - use all matchsticks to make one square
            - square: 4 equal partitions
        - no greedy optimal approach to determine optimal placement
            - small elements does not mean easier or possible to partition
        
        idea - backtracking
        - try to partition into 4 sums
        - use each matchstrick ONLY once
        - must use ALL matchsticks
        note: there is duplicates -> must skip and handle
        - don't need keep track of all 4 paritions
            - track 3 and complement the 4th

        i is the position in the input
        dfs(i, part1, part2, part3, part3):
            base case if no more elements or if found match, which ever earlier

            for j in range(i, n):
                if cur is same as previous element -> skip duplicate processing at this iteration
                    - let the previous element path get cover the search for the duplicate

                try put in every partition

        duplicates
        - you can use them but in separate recursions -> like new level in the recursion tree
        - you should not use duplicates within the same level

        there are two kinds
        - no duplicate elements [1,2,2]
            - duplicate comes with reprocessing elements behind you. eg 1,2 and 2,1 for combination is the same
        - duplicate elemtent, same issue but additional same level [1,1,2]
            - you can either [1,x,2] or [x,1,2] both are the same
                - it is not the above problem of procesing backwards.
                - it is the issue where same level selection in the output should not
                    look at duplicate elements as further down would have repeats
                - cross level for different output state is ok

        optimisations
        1) early pruning: if total can't be divided by 4 -> invalid 
        2) Early return if anyone gets True instead of waiting for all then check if any true
        3) Sort matchsticks and go through largest first -> fail faster

        notice: you MUST use all elements so there is NO SKIPPING
            - 
        """
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        matchsticks.sort(reverse=True) # largest first

        # ignore part 4 as it is the complement
        def dfs(i, part1, part2, part3): # return Boolean
            # 1) Base cases: no more sticks to use OR found the answer
            if part1 == part2 == part3 == (total - part1 - part2 - part3): # valid
                return True
            if i >= n: # no more elements -> reached here means prev did not find valid
                return False

            # 2) main loop
            result_bool = False
            for j in range(i, n):
                if j != i and matchsticks[j-1] == matchsticks[j]: # handle duplicate
                    continue

                # try all partitions
                cur = matchsticks[j]
                if dfs(j + 1, part1 + cur, part2, part3):
                    return True
                if dfs(j + 1, part1, part2 + cur, part3):
                    return True
                if dfs(j + 1, part1, part2, part3 + cur):
                    return True
    
            return False # if not True found
        return dfs(0, 0, 0, 0)
        






        # unoptimised for early returns
        """
        n = len(matchsticks)
        total = sum(matchsticks)

        # ignore part 4 as it is the complement
        def dfs(i, part1, part2, part3): # return Boolean
            # 1) Base cases: no more sticks to use OR found the answer
            if part1 == part2 == part3 == (total - part1 - part2 - part3): # valid
                return True
            if i >= n: # no more elements -> reached here means prev did not find valid
                return False

            # 2) main loop
            result_bool = False
            for j in range(i, n):
                if j != i and matchsticks[j-1] == matchsticks[j]: # handle duplicate
                    continue

                # try all partitions
                cur = matchsticks[j]
                bool1 = dfs(j + 1, part1 + cur, part2, part3)
                bool2 = dfs(j + 1, part1, part2 + cur, part3)
                bool3 = dfs(j + 1, part1, part2, part3 + cur)
            
                if bool1 or bool2 or bool3:
                    result_bool = True
            return result_bool
        return dfs(0, 0, 0, 0)
        """