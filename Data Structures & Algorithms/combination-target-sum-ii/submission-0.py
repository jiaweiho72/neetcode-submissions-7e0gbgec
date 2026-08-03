class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        30 Jun 2026
        - return unique combinations (not permutations) of candidates where they sum to target
        - diff between combination sum I: can't rechoose candidates (choose at most once)
            - don't rechoose the same element
            - now must handle duplicates

        note:
        - each candidate only used once
        - combination
        - candidates may have duplicates

        idea:
        - return all -> backtracking
            - use or don' use
        - to prevent duplicate
            - sort 
            - Use or don't use
                - if use means next round determine if want to use or don't use again
                - if don't use means really don't use anymore duplicates
                    - so skip all duplicates
                this prevents the case where example index 1,2,3,4 has duplicates and
                you use 1,2 and 3,4
                    - this prevents this case where at 1 you choose to not use -> skips 2,3,4

                makes it linear to only have one linear combination check and prevent the permutations
        """

        n = len(candidates)

        candidates.sort()
        result = []
        combination = []

        total = 0
        def backtracking(i):
            nonlocal total
            if total == target:
                result.append(combination.copy())
                return
            if total > target or i > n - 1: # invalid / out of bounds
                return

            cur = candidates[i]
            
            # 1) use 
            combination.append(cur)
            total += cur
            backtracking(i + 1)

            # 2) or don't use
            combination.pop()
            total -= cur
            # handle duplicate
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i = i + 1
            backtracking(i + 1)

        backtracking(0)
        return result


            




        # Looks like 2/3sum but it can be any number of elements
        # Idea: dfs recursion
        # In order to prevent duplicates:
        # - skip already used candidates
        # - if there are duplicate candidates, have to skip them too

        # n = len(candidates)
        # result = []
        # candidates.sort()
        # def dfs(index, cur, total):
        #     # Base case
        #     if total == target:
        #         result.append(cur.copy())
        #         return

        #     if total > target or index == n:
        #         return # Did not meet target and will never -> stop the loop
        #     # Two cases:

        #     # 1) We select the current element at index
        #     selected = candidates[index]
        #     cur.append(selected)
        #     dfs(index + 1, cur, total + selected)

        #     # 2) We don't select and select the next element
        #     # But we skip if the element is duplicate and has been ran before
        #     cur.pop() 
        #     while index + 1 < n and candidates[index] == candidates[index + 1]:
        #         index += 1

        #     # Explore the next element after skipping duplicates
        #     dfs(index + 1, cur, total)

        # dfs(0, [], 0)
        # return result

        """
        Speed Run
        - Same as ComSum I -> now is only can use once

        - backtracking
            - keep track of cur sum
            - index to move on to next candidate
        - to address duplicate
            - sort first as you don't need to backtrack in order
            - while loop like in 3sum to ignore duplicates
        - similar to ComSum, you need to keep track of the sum as well as the list of elements as you need to return the elements
        """

        n = len(candidates)
        res = []

        candidates.sort()
        def backtracking(total, i, cur):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == n: # invalid
                return
            
            # 1) include current
            cur.append(candidates[i])
            backtracking(total + candidates[i], i + 1, cur)

            # 2) exclude current
            """
            because if you don't don't use cur and next == cur, then it is a repeat
            - different from 1) where you used cur and use next
            """
            cur.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            backtracking(total, i + 1, cur)
        backtracking(0, 0, [])
        return res