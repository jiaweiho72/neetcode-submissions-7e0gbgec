class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        11 Sep 2026
        - return all possible combinations of k numbers chosen from 1-n

        go through every 1-n
        - inclusive of n
        - instead of returning all sizes like in combination
            - add to result list only when size == k
        - input no duplicate so no need to handle and skip


        idea of forloop
        - once you choose this element j, you never choose it again
            - so the search space decreases.
            - don't include it or the previous elements
                - previous one is handled by previous elements
            like you choose j for current
            - there won't be another exact case where the front part is the same and it choose j again, not possible
        
        time: O(2^n) 
        space: O(2^n) stack
        10mins
        """
        result = []
        def dfs(i, cur):
            # 1) base case
            if len(cur) == k:
                result.append(cur.copy())
                return

            # 2) main loop
            for j in range(i, n + 1): # j includes i too
                # NA - violates constraint

                # add current j element
                cur.append(j)
                dfs(j + 1, cur)
                cur.pop()

        dfs(1, [])
        return result





